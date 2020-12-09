# set up the LoRa Radio

from machine import Pin, SPI
from lora.lora_config import * #import the pin configuration
from lora.sx127x import SX127x
from time import sleep
try:
    from rfid.rfid_simple_reader import scan
except ImportError:
    pass

class LoRaRadio:
    def __init__(self,spi,ss):
        self.lora = SX127x(spi,ss,pins=device_config, parameters=lora_parameters)
        self.lora.set_spreading_factor(12) #Max Range
        
        
    def receive(self,display=None):
        if display:
            display.show_text("LoRa Receiver")

        while True:
            if self.lora.received_packet():
#                 self.lora.blink_led()
                print('something here')
                payload = self.lora.read_payload()
                print(payload)
                if display:
                    display.clear()
                    display.show_text(payload)
                    
                    
    def send(self,display=None):
        counter = 0
        print("LoRa Sender")
        if display:
            display.show_text("LoRa Sender")
            sleep(1)

        while True:
            payload = ''
            try:
                payload = scan() + ' : ' + str(counter)
            except Exception as e:
                print('scan not available: {}'.format(str(e)))
                
            if payload:
                print("Sending packet: \n{}\n".format(payload))
                if display:
                    display.clear()
                    display.show_text('Sending Packet...')
                    display.show_text(payload,y=12)
#                     display.show_text("RSSI: {}".format(self.lora.packet_rssi()),y=24)
                    display.show_text("Counter: {}".format(counter),y=36)
                    
                self.lora.println(payload)

                counter += 1
                sleep(1)
