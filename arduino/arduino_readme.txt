# Testing with Arduino

Loaded code from https://github.com/YogoGit/TTGO-LORA32-V1.0

Ran just fine. but with spreading factor of 12 (max) best test was .65km (.4mi) with the transmitter 
sitting on the edge of my garage roof. (10'?)

Could try a taller mast and better antenna, but at a minimum I need to reach 3km range doubt I would 
get that consistently.

Also tried increasing to error correction setting to the max, thinking that might help. No improvement in 
range. Maybe just data integrity but I did not try to measure that. Not at all sure if it would matter without
code on the receiver side. Changing the correction setting on only one unit did not seem to effect the 
ability of the other unit to receive the message. May be a transmit only setting.

Note about programming:
There is nothing extra to do when programming the device with Arduino IDE or micropython. Just treat the device
as new and re-program. Use `esptool.py --port <port> erase_flash` first to clear everything out