import rclpy
from rclpy.node import Node
from rt2string_msg.msg import RT2String
from std_msgs.msg import Int32, String


class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('palindrome_checker')

        self.result_publisher = self.create_publisher(
            Int32, '/palindrome_result', 10
        )

        self.string_subscription = self.create_subscription(
            RT2String, '/rt2_string', self.check_palindrome, 10
        )

        self.response_subscription = self.create_subscription(
            String, '/palindrome_response', self.show_response, 10
        )

    def check_palindrome(self, msg):
        text = msg.data
        cleaned = text.replace(' ', '').lower()
        result = Int32()
        result.data = 1 if cleaned == cleaned[::-1] else 0

        self.result_publisher.publish(result)
        self.get_logger().info(
            f'Input: {text} | Sent result: {result.data}'
        )

    def show_response(self, msg):
        self.get_logger().info(f'Final answer: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
