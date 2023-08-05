"""
from time import sleep 
from adafruit_servokit import ServoKit
kit = ServoKit(channels = 16)
print("Servos Running")
import threading

def start():
    
    def head():
        kit.servo[0].angle= 0
        sleep(1)
        kit.servo[0].angle= 100
        sleep(1)
        kit.servo[0].angle= 0
        sleep(1)
        kit.servo[0].angle= 100
        sleep(1)
        kit.servo[0].angle= 50
        sleep(1)
    
    head()
        
    def right_hand():
        kit.servo[4].angle= 100
        sleep(1)
        kit.servo[5].angle= 70
        sleep(1)
        kit.servo[6].angle= 0
        sleep(1)
        
    def left_hand():
        kit.servo[1].angle= 0
        sleep(1)
        kit.servo[2].angle= 100
        sleep(1)
        kit.servo[3].angle= 180
        sleep(1)

    def right_home():
        kit.servo[6].angle= 100
        sleep(1)
        kit.servo[5].angle= 0
        sleep(1)
        kit.servo[4].angle= 30
        sleep(1)
        
    def left_home():
        kit.servo[3].angle= 80
        sleep(1)
        kit.servo[2].angle= 150
        sleep(1)
        kit.servo[1].angle= 80
        sleep(1)
        
        
    #left_hand()
    #right_hand()
    #right_home()
    #left_home()

    def namaste():
        
        left_thread = threading.Thread(target= left_hand)
        right_thread = threading.Thread(target= right_hand)

        left_thread.start()
        right_thread.start()
        
    def home():
        
        left_h_thread = threading.Thread(target= left_home)
        right_h_thread = threading.Thread(target= right_home)

        left_h_thread.start()
        right_h_thread.start()

    print("servos running test ")
    namaste()
    home()

start()


"""

print("Servos Running for Test in with Application")