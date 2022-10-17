from fhict_cb_01.CustomPymata4 import CustomPymata4
import time

DHTPIN = 12
BUTTON1PIN = 8
REDLEDPIN = 4

pressedButton = []

def countdown(t):
    t = 600    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      

countdown(int(t))

def setup():
    global board
    board = CustomPymata4(com_port = "COM11")
    board.set_pin_mode_digital_input_pullup(BUTTON1PIN)
    board.set_pin_mode_digital_output(REDLEDPIN)

def loop():
    level, time_stamp = board.digital_read(BUTTON1PIN)
    pressedButton.append(level)
    print(level)

    if (level == 0):
        board.digital_pin_write(REDLEDPIN, 1)
        time.sleep(0.5)
        board.digital_pin_write(REDLEDPIN, 0)
        time.sleep(0.5)



#--------------
# main program
#--------------
setup()
while True:
    loop()  
  