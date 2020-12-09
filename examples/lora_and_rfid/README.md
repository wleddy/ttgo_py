# Using LoRa radio and RFID Reader

This is a simple exercise to try using the LoRa radio on the TTGO with a RFID reader (MFRC522)
connected to the SPI bus.

To install on the device, copy the contents of this directory into `lib` on the device. That puts it into
the

To start the program running, put the following into the device `main.py` module:

```
    import lora_rfid_main as my_radio

    my_radio.start('receiver') # or 'sender'
    
```

The built in LoRa radio and the RFID reader share the bus so each must have a ss pin set but the
radio's ss pin is pre-set to GIOP 18. The reader must set another pin.

The ss pin setup should be Pin.OUT, Pin.PULL_DOWN at initialization.

It's important to add 10k ohm pullup resistors between vcc and the ss pin of each SPI connected device.

Some wierdness... from my reading multiple slave devices on the SPI bus can share 
SCK, MOSI, & MISO with SS as a separate connection to each device. So far I have only
been able to get them to work with MOSI for the radio on 27, and MOSI for the rfid reader
on 23. Also, SS should be able to be any bidirecional pin not used eslewhere, but I 
can only get the rfid reader working with SS on 17.
