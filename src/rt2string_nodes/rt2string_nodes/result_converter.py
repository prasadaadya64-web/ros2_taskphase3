import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String


class ResultConverter(Node):
    def __init__(self):
        super().__init__('result_converter')

        self.response_publisher = self.create_publisher(
            String, '/palindrome_response', 10
        )

        self.result_subscription = self.create_subscription(
            Int32, '/palindrome_result', self.convert_result, 10
        )

    def convert_result(self, msg):
        response = String()
        response.data = 'Yes' if msg.data == 1 else 'No'

        self.response_publisher.publish(response)
        self.get_logger().info(f'Sent response: {response.data}')


def main(args=None):
    rclpy.init(args=args)
    node = ResultConverter()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
