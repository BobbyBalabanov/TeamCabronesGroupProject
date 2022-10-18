# from curses import BUTTON1_CLICKED
from tracemalloc import start
from fhict_cb_01.CustomPymata4 import CustomPymata4
import time

DHTPIN = 12
BUTTON1PIN = 8
LEDPIN = [4,5]
level = 1
prevLevel = 0
count = 120


pressedButton = []

def timer():
    global count
    while count >= 0:
        board.displayShow(str(count).zfill(4))
        count -= 1
        board.digital_pin_write(3, 1)
        time.sleep(0.1)
        board.digital_pin_write(3, 0)
        time.sleep(0.1)
        time.sleep(0.8)
    count = 120  

def ButtonChanged(data):
    global level
    level = data[2] # get the level
    # Keep the callback function short and fast.
    # Let loop() do the 'expensive' tasks.
       

def setup():
    global board
    board = CustomPymata4(com_port = "COM11")
    board.set_pin_mode_digital_input_pullup(BUTTON1PIN, callback = ButtonChanged)
    for pin in LEDPIN:
        board.set_pin_mode_digital_output(pin)

def loop():
    global prevLevel
    # Only print button level when level changed.
    if (prevLevel != level):
        prevLevel = level
    if (level == 0):
            board.digital_pin_write(LEDPIN[1],0)
            board.digital_pin_write(LEDPIN[0],1)
            timer()
            board.digital_pin_write(LEDPIN[1],1)
            board.digital_pin_write(LEDPIN[0],0)


        


#--------------
# main program
#--------------
setup()
while True:
    loop()
  