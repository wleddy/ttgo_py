from machine import Pin, I2C
from upy_sensors import ssd1306 # oled display

i2c = I2C(scl=Pin(15), sda=Pin(4))

try:
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
except Exception as e:
    print(str(e))
    
print('nodes found:')

i2c.scan()
# oled.fill(1)
# oled.show()
