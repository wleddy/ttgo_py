import machine
from wifi_connect import ConnectWifi
from time import sleep

ConnectWifi(debug=True).connect()

led = machine.Pin(2,machine.Pin.OUT)

x = 0
while x < 5:
    led.value(not led.value())
    sleep(.5)
    x +=1
    
led.off()
del x

    