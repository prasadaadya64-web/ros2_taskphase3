import rclpy
from rclpy.node import Node
from taskone_msg.msg import TaskOne


class TaskOneSubscriber(Node):

    def __init__(self):
        super().__init__('taskone_subscriber')

        self.subscription = self.create_subscription(
            TaskOne,
            '/taskone',
            self.calculate_speed,
            10
        )

    def calculate_speed(self, msg):
        speed = msg.ang_vel * msg.radius

        self.get_logger().info(
            f'Angular velocity = {msg.ang_vel}, '
            f'Radius = {msg.radius}, '
            f'Longitudinal speed = {speed} m/s'
        )


def main(args=None):
    rclpy.init(args=args)

    node = TaskOneSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
