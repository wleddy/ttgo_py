from machine import Pin, PWM
import time
import uasyncio as asyncio
        
        
class Pulsar:
    FAST = .05
    MEDIUM = .1
    SLOW = .2
    
    def __init__(self,pin=2,bright=500,dim=25,rate='MEDIUM'):
        self.pin = pin
        self.bright = bright
        self.dim = dim
        self.rate = self.MEDIUM
        self.step = int(self.bright / 10)
        if isinstance(rate,str):
            rate = rate.upper()
            if rate == 'FAST':
                rate = self.FAST
            elif rate == 'SLOW':
                rate = self.SLOW
        elif isinstance(rate,(int,float)):
            rate = float(rate)
        else:
            raise ValueError('Rate must be "slow","medium","fast", or a number')
        
        self.led = PWM(Pin(pin),duty=0,freq=60)
        self.stop = False 
        self.reverse = False
        self.pause_pulse = True # call start() to unpause
        
    def off(self):
        start = self.led.duty()
        self.pause_pulse = True
        self.reverse = False
        for x in range(start,self.dim,-10):
            self.led.duty(x)
            time.sleep(self.FAST)
            
        self.led.duty(0)
        print('led off')
        
    def start(self):
        self.stop = False
        self.pause_pulse = False
        self.led.duty(0)
        
    def end(self):
        self.stop = True
                
        
    async def pulse(self):
        if self.pause_pulse and not self.stop:
            await asyncio.sleep(.5)
        else:
            while not self.stop:
                dir = -1 if self.reverse else 1
                new_val = self.led.duty() + (self.step * dir)
                if new_val <= self.dim:
                    new_val = self.dim
                    self.reverse = False
                elif new_val >= self.bright:
                    new_val = self.bright
                    self.reverse = True
                
                if not self.pause_pulse:
                    self.led.duty(new_val)
                    print('pulse...{}'.format(new_val))
                    await asyncio.sleep(self.MEDIUM)

        
led = Pulsar()

async def do_something_else():
    led.start()
    for x in range(10):
        print('working...{}'.format(x))
        await asyncio.sleep(1)
    led.off()

async def main():
    #led.start()
    await asyncio.gather(*(
        led.pulse(),
        do_something_else(),
        )
    )
    
led.start()
asyncio.run(main())
led.end()
