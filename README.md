# ttgo_py

11/21/20 -- Some initial experiments with the TTGO LoRa board.


## My Notes:

### RTC

First create the RTC with something like now = RTC()

Then you can set the time with the command `now.datetime((2020,11,26,-8,10,15,0,0))` 
which will set the clock to 11/26/2020 10:15 AM. 

The 4th value seems to be required, but in my case seems to always be converted to '3'
when you call `now.datetime()` => '(2020,11,26,3,10,15,0,0)'


### network.WLAN

When creating an access point, create the access point object then if you want to set the config
you just activate it first with `ap.active(True)` or you will get an error.

AP password does not seem to be set, but you can set the name

After you create the object, you can get the value with `config('essid')


### I2C

-- Update 12/6/20 - i2c bus is also available on GPIO 4 (sda) and 15 (slc). Pins 18 (scl) and 19 (sda) also worked
but they are used for SPI communication with the built in LoRa radio, so I should not be using those, I think.

### SPI

Pins:
    Here's a handy dictionary to set all the pins (These work with the built in LoRa radio)
    ```device_config = {
            'miso':19,
            'mosi':27,
            'ss':18,
            'sck':5,
            'dio_0':26,
            'reset':14,
        }```
        
    

To solder the headers to 18 and 19 you need to unscrew the OLED mounting piece and pull the display and
ribbon cable away a bit (use some tape) so that you can access the pads.

When setting the device ID, need to pass the ID in decimal rather than hex. All the examples I see
use Hex, but it does not work with my boards. So, the ssd1306 OLED display is id 60, not x03c. I was
able to connect with the PFC8574 port extender on id 32, not x020.

### ssd1306 OLED

There does not seem to be a way to clear part of the display to display new text. You need to clear the
whole screen and redisplay everything. The characters seem to have a transparent background so if you print
on top of existing chars they just overlay. A space char will not blank out a previously displayed char either. I 
tried that.

### Battery Power (not tested yet)

My reading indicates that you can apply 5v to 10v to VIN which is not marked on this board. My guess is that you
can apply it to the 5v pad, but maybe not. In an case you would then not have a 5v regulated source.

From other people's experience, 10v is really the upper limit.