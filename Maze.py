import Leap, sys, serial
import pygame
from pygame.locals import *
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

#Serial Connection

port = '/dev/ttyS0'

serialPort = serial.Serial(port,9600)


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
        print "Frame available"
        
        frame = controller.frame()
        #Process frame data
        if len(frame.hands) == 0:
            serialPort.write("x:"+90)
            serialPort.write("z:"+90)
        else:
            print "x: ",
            print hand.palm_position.x,
            print ", z: ",
            print hand.palm_position.z
            serialPort.write("x:"+conversion(hand.palm_position.x))
            serialPort.write("z:"+conversion(hand.palm_position.x))


def conversion(coordinate):
    return 90 - int(coordinate/10)

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