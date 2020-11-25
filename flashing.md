# First flash

11/21/20

Following instructions on http://micropython.org/download/esp32/

Erase flash with:

```esptool.py --chip esp32  erase_flash```
 
This detected the serial port: 

```/dev/cu.SLAB_USBtoUART```
 
Did firmware install as:

```esptool.py --chip esp32 --port /dev/cu.SLAB_USBtoUART  --baud 460800 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin```


During firmware flash esptool.py reported:

```
Chip is ESP32-D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 26MHz
MAC: ac:67:b2:1a:69:4c
```

