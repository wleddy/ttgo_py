# Simple test to try out the LoRa Radio and the RFID reader
from lora.lora_radio import LoRaRadio 
from ssd1306_display.ssd1306_i2c_bl import Display
from spi_setup.spi_setup import get_spi

        
def start(mode): # mode == 'receiver' or 'sender'
    # if mode == 'receiver' the radio swithes on and waits for anyting it hears
    #   displays the data received on the built in OLED display
    # if mode == 'sender' wait for RFID tag to be present and send the uid
    #   out over the radio
    #
    # Both methods loop forever
    spi,ss = get_spi('ttgo')
    print(spi)
    print(ss)
    
    display = Display()

    lr = LoRaRadio(spi,ss)
    lora = lr.lora
    if mode == 'receiver':
        lr.receive(display=display)
    elif mode == 'sender':
        lr.send(display=display)
    else:
        print("'{}' is not a valid mode".format(mode))

