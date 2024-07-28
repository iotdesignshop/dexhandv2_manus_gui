import rclpy
from rclpy.node import Node
from std_msgs.msg import String 
from dexhandv2_control.srv import Reset
import tkinter as tk

class GuiNode(Node):
    def __init__(self):
        super().__init__('gui_node')
        self.publisher_ = self.create_publisher(String, 'dexhand_manus_cmd', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.root = tk.Tk()
        self.root.title("DexHand Manus Control")
        self.root.geometry("800x200")

        # Hand reset service
        self.reset_srv = self.create_client(Reset, '/dexhandv2/reset')
        while not self.reset_srv.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Hand reset service not available, waiting again...')
        self.reset_req = Reset.Request()


        tk.Button(self.root, text="Reset Origin", command=self.publish_reset_message).pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Button(self.root, text="Reset Hand Hardware", command=self.publish_reset_hardware_message).pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        #tk.Button(self.root, text="Close", command=self.close_gui).pack()

    def timer_callback(self):
        self.root.update()

    def publish_reset_message(self):
        msg = String()
        msg.data = 'reset_origin'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

    def publish_reset_hardware_message(self):
        self.reset_req.id = 'all'
        self.reset_srv.call_async(self.reset_req)
        self.get_logger().info('Resetting hand hardware...')

    def close_gui(self):
        self.root.quit()
        self.root.destroy()
        self.destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = GuiNode()
    try:
        rclpy.spin(node)
    except tk.TclError:
        # Handle the exception when the GUI is closed
        node.get_logger().info('GUI has been closed.')
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
