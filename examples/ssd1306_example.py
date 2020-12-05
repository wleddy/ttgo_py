from machine import Pin, I2C
import time
import ssd1306_i2c_bl

oled_addr = 60

buf = bytearray(1)
d_dur = .2

oled = ssd1306_i2c_bl.Display()
oled.show_text("Hello World!",hold_seconds = 1)
    
def display(txt,x=0,y=0,show=True,clear=False):
    oled.show_text(txt,x,y,clear_first=clear,show_now=show)

def display_clear():
    oled.clear()

def disco():
    display_clear()
    oled.display.invert(1)
    display('Disco Baby!!!',y=16,x=10)
    for y in range(2):
        time.sleep(d_dur*4)
        display_clear()
     
    oled.display.invert(0)
    display_clear()

x = 1
limit = 128
direction = 1
char_width = 7
char_height = 12
while x < limit+1:
    display_clear() # You have to clear the whole display as far as I can tell
    display("Precheck: {}".format(x),show=False)
    if x < 1:
        direction = 1
        x = 2 #was 1 at loop start, so this has to be a restart
    if x > limit:
        x = limit/2
        direction = -1
    disp = "Up" if direction == 1 else "Down"
    display("Direction: {}".format(disp),y=char_height,show=True)
    if x == 1:
        disco()
    # subtract x from 'all_off' (255) to turn on one led
    time.sleep(d_dur)
    if x < limit and direction == 1:
        x = x*2
    else:
        direction = -1
        x = x/2

