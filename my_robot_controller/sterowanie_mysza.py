import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class MouseControlNode(Node):
    def __init__(self):
        super().__init__('sterowanie_mysza')
        # Subskrypcja obrazu (z kamery lub symulacji)
        self.subscription = self.create_subscription(Image, '/image_raw', self.image_callback, 10)
        # Publikacja komend ruchu do robota
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.bridge = CvBridge()
        
        # Tworzenie okna OpenCV
        cv2.namedWindow("Interfejs")
        cv2.setMouseCallback("Interfejs", self.mouse_event)
        self.get_logger().info("Node gotowy! Kliknij gore okna, by jechac w przod, dol, by w tyl.")

    def mouse_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            msg = Twist()
            height = 480 # Standardowa wysokosc okna
            if y < height / 2:
                msg.linear.x = 0.3  # Predkosc do przodu
                self.get_logger().info("Ruch: PRZÓD")
            else:
                msg.linear.x = -0.3 # Predkosc do tyłu
                self.get_logger().info("Ruch: TYŁ")
            self.publisher.publish(msg)

    def image_callback(self, msg):
        # Konwersja obrazu z ROS na format OpenCV
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        h, w, _ = cv_image.shape
        # Rysujemy linię pomocniczą na środku
        cv2.line(cv_image, (0, h//2), (w, h//2), (0, 0, 255), 2)
        cv2.imshow("Interfejs", cv_image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = MouseControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
