import Leap, sys, serial
import pygame
from pygame.locals import *
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

#Serial Connection

port = '/dev/tty.usbmodem1421'

serialPort = serial.Serial(port,9600)

done = 0

#Listener
class LeapEventListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);        
        controller.config.set("Gesture.Swipe.MinLength", 200.0)
        controller.config.save()


    def on_disconnect(self, controller):
        print "Disconnected"

    def on_frame(self, controller):
        global done
        print "Frame available"
        
        frame = controller.frame()
        #Process frame data
        if len(frame.hands) == 0 and done == 0:
            serialPort.write("x:"+str(90))
            serialPort.write("z:"+str(90))
            done = 1
        else:
            done = 0
            hand = frame.hands[0]
            print hand.palm_position.x,
            print ", z: ",
            print hand.palm_position.z
            print conversion(hand.palm_position.x)
            print conversion(hand.palm_position.z)
            serialPort.write(conversion(hand.palm_position.x)+"\n")
            serialPort.write(conversion(hand.palm_position.z)+"\n")


def conversion(coordinate):
    return str(int((coordinate+270)/3))

def main():
    listener = LeapEventListener()
    controller = Leap.Controller()

    controller.add_listener(listener)

    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()