from machine import Pin, I2C
import time
import ssd1306_i2c_bl

px_addr = 32
oled_addr = 60

try:
    # configure the port extender @ 0x20
#     oled = I2C(0,scl=Pin(15), sda=Pin(4), freq=400000)
    px = I2C(scl=Pin(18), sda=Pin(19), freq=400000)
except Exception as e:
    print(str(e))
    
print('Expander Bus found:')
px.scan()
# print("oled bus")
# oled.scan()

buf = bytearray(1)
d_dur = .2

oled = ssd1306_i2c_bl.Display()
oled.show_text("Hello World!",hold_seconds = 1)
# buf[0] = 1
# oled.display.fill(0x01)


def all_off():
    set_leds(255)
    
def all_on():
    set_leds(0)
    
def set_leds(x):
    buf[0] = int(x)
    temp = px.writeto(px_addr,buf)
    
def disco():
    display_clear()
    oled.display.invert(1)
    display('Disco Baby!!!',y=16,x=10)
    for y in range(2):
        all_on()
        time.sleep(d_dur)
        all_off()
        time.sleep(d_dur)
     
    oled.display.invert(0)
    display_clear()
    
    
def display(txt,x=0,y=0,show=True,clear=False):
    oled.show_text(txt,x,y,clear_first=clear,show_now=show)

def display_clear():
    oled.clear()
    
all_off()
x = 1
limit = 128
direction = 1
char_width = 7
char_height = 12
while x < limit+1:
    display_clear()
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
    set_leds(255-x)
    time.sleep(d_dur)
    if x < limit and direction == 1:
        x = x*2
    else:
        direction = -1
        x = x/2

