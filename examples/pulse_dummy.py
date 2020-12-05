#from machine import Pin, PWM
import time
import asyncio
import pdb
try:
    import this
except ImportException as e:
    pass


class Pin:
    def __init__(self,id=2):
        self.id = id
        
class PWM:
    def __init__(self,pin,duty=100,freq=4000):
        self.pin = pin
        self.duty_cycle = duty
        self.freq=freq
        
    @property
    def duty(self):
        return self.duty_cycle
        
    @duty.setter
    def duty(self,level):
        self.duty_cycle = level
        
        
        
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
        self.stop = True # start off in off position
        self.reverse = False
        
    def off(self):
        start = self.led.duty_cycle
        self.stop = True
        self.reverse = False
        for x in range(start,0,10):
            self.led.duty_cycle = x
            time.sleep(FAST)
            
        self.led.duty_cycle = 0
        print('led off')
        
    def start(self):
        self.stop = False
        
        
    async def pulse(self):
        if self.stop:
            self.off()
            self.stop = False
            while not self.stop:
                for d in range(self.dim,self.bright,self.step):
                    self.led.duty_cycle = d
                    await asyncio.sleep(self.rate)
                for d in range(self.bright-self.step,self.dim,self.step * -1):
                    self.led.duty_cycle = d
                    await asyncio.sleep(self.rate)
                    
                    
    async def pulse2(self):
        while not self.stop:
            dir = -1 if self.reverse else 1
            new_val = self.led.duty_cycle + (self.step * dir)
            if new_val <= self.dim:
                new_val = self.dim
                self.reverse = False
            elif new_val >= self.bright:
                new_val = self.bright
                self.reverse = True
            
            self.led.duty_cycle = new_val
            print('pulse...{}'.format(new_val))
            await asyncio.sleep(self.MEDIUM)
            # pdb.set_trace()

        
led = Pulsar()

async def do_something_else():
    for x in range(10):
        print('working...{}'.format(x))
        await asyncio.sleep(1)
        
    led.off()


async def main():
    await asyncio.gather(*(
        led.pulse2(),
        do_something_else(),
        )
    )
    
led.off()
led.start()
asyncio.run(main())
led.off()
