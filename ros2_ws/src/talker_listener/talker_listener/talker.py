import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(String, 'chatter', 10)
        self.count = 0
        self.create_timer(1.0, self.tick)

    def tick(self):
        msg = String(data=f'hello {self.count}')
        self.pub.publish(msg)
        self.get_logger().info(f'sent: {msg.data}')
        self.count += 1


def main():
    rclpy.init()
    rclpy.spin(Talker())


if __name__ == '__main__':
    main()
