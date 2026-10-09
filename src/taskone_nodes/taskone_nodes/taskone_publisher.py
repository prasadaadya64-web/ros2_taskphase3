import rclpy
from rclpy.node import Node
from taskone_msg.msg import TaskOne


class TaskOnePublisher(Node):

    def __init__(self):
        super().__init__('taskone_publisher')

        self.publisher = self.create_publisher(TaskOne, '/taskone', 10)
        self.timer = self.create_timer(1.0, self.publish_data)

        self.ang_vel = 0.0
        self.radius = 0.0

    def publish_data(self):
        msg = TaskOne()
        msg.ang_vel = self.ang_vel
        msg.radius = self.radius

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Published: angular velocity = {self.ang_vel}, radius = {self.radius}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = TaskOnePublisher()

    node.ang_vel = float(input('Enter angular velocity: '))
    node.radius = float(input('Enter wheel radius: '))

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
