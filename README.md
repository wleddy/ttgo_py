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

Was able to get I2C working on GIPO 18 (scl) and 19 (sda). GIPO 25 (slc) and 26 (sda) are supposed to work
but I could not communicate using them. They did not return good device id's with .scan() function. Read
a comment that the behavior I was seeing (list of many ids) may be an indication of a bad connection, but
once I switched to ports 18 and 19 the problem went away without any connection changes.

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