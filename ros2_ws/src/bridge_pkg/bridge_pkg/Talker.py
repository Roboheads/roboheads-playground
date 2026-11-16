import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_srvs.srv import Trigger
from bridge_interfaces.srv import SetCounter

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(String, 'hello', 10)
        self.timer = self.create_timer(1.0, self.tick, autostart=True)
        self.count = 0
        self.reset_srv = self.create_service(SetCounter, 'set_counter',  self.on_reset)
    
    def on_reset(self, request, response):
        response.previous = self.count
        self.count = request.value
        self.get_logger().info(f'Counter reset to {self.count}')
        return response

    def tick(self):
        msg = String()
        msg.data = f'Hello, world! {self.count}'
        self.pub.publish(msg)
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    rclpy.shutdown()
