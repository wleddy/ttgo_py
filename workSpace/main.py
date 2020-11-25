import machine
from wifi_connect import ConnectWifi
from time import sleep

ConnectWifi(True).connect()

led = machine.Pin(25,machine.Pin.OUT)

while True:
    led.value(not led.value())
    sleep(.5)
    