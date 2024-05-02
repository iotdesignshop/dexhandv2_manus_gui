import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import tkinter as tk
from tkinter import simpledialog

class GuiNode(Node):
    def __init__(self):
        super().__init__('gui_node')
        self.publisher_ = self.create_publisher(String, 'dexhand_manus_cmd', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.root = tk.Tk()
        self.root.title("DexHand Manus Control")
        self.root.geometry("800x200")

        tk.Button(self.root, text="Reset Origin", command=self.publish_reset_message).pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        #tk.Button(self.root, text="Close", command=self.close_gui).pack()

    def timer_callback(self):
        self.root.update()

    def publish_reset_message(self):
        msg = String()
        msg.data = 'reset_origin'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

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
