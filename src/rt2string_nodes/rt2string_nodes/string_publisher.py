import rclpy
from rclpy.node import Node
from rt2string_msg.msg import RT2String


class StringPublisher(Node):
    def __init__(self):
        super().__init__('string_publisher')
        self.publisher = self.create_publisher(
            RT2String, '/rt2_string', 10
        )
        self.text = ''
        self.timer = self.create_timer(1.0, self.publish_string)

    def publish_string(self):
        msg = RT2String()
        msg.data = self.text
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: {self.text}')


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()
    node.text = input('Enter a string to check: ')

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
