import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.count = 0
        self.sub = self.create_subscription(String, 'hello', self.on_msg, 10)

    def on_msg(self, msg):
        self.count += 1
        self.get_logger().info(f'I heard: "{msg.data}"')

    
def main(args=None):
    rclpy.init(args=args)
    node = Listener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
