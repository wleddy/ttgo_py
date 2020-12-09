from utime import sleep
from machine import Pin

from rfid.mfrc522 import MFRC522
from spi_setup.spi_setup import get_spi
from ssd1306_display.ssd1306_i2c_bl import Display

display = Display()
display.show_text("Please Wait...")
# Application is to auto-run on power-up it can be necessary to add a short delay
sleep(5)

# sck = Pin(5, Pin.OUT, Pin.PULL_DOWN)
# copi = Pin(23, Pin.OUT)
# cipo = Pin(19, Pin.OUT)
# spi = SPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=copi, miso=cipo)
reader = None
# cs = Pin(17, Pin.OUT) # AKA: cs ss sda etc...
spi,ss = get_spi('ttgo_rfid')
print(spi)
print(ss)
reader = MFRC522(spi, ss)

def init(spi):
    global reader
    # micropython's docs say not to use this pin for sda,
    #  but it's the only one I found that works
    cs = Pin(17, Pin.OUT) # AKA: cs ss sda etc...
    reader = MFRC522(spi, cs)


def awaiting_card():
    display.show_text("Awaiting Tag")
    
def show_result(result,dwell=3):
    display.clear()
    display.show_text(result)
    sleep(dwell)
    display.clear()
    awaiting_card()
    
def scan():
    display.clear()

    while True:
        sleep(1) # give reader a little quiet time
        awaiting_card()
        (status, tag_type) = reader.request(reader.CARD_REQIDL)
        if status == reader.OK:
            # tag has been detected at this point, but not read
            display.clear()
            display.show_text_wrap("Tag present, type: {}".format(tag_type))
            sleep(1)
            display.clear()
            (status, raw_uid) = reader.anticoll()
            if status == reader.OK:
                if reader.select_tag(raw_uid) == reader.OK:
                    # convert int list to hexidecimal string
                    uid = ('%02x%02x%02x%02x' % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
#                     print('raw_uid; {}'.format(raw_uid))
#                     print('uid: %s' % uid)
                    status = "Got: {}".format(uid)
                    ##########################
                    # Do something with uid ##
                    ##########################
#                     display.clear()
#                     display.show_text(status)
#                     sleep(.5)
                    
                    return uid
                    
                else:
                    status = 'FAILED TO SELECT TAG'
    #             sleep_ms(100)
                show_result(status)


