from instance.secrets import Secrets
from time import sleep
import network

class ConnectWifi():
    #Simple connection script
    def __init__(self,debug=False):
        secrets = Secrets()
        self.ssid_ = secrets.wifi_ssid
        self.wp2_pass = secrets.wifi_pass
        self.sta_if = network.WLAN(network.STA_IF)
        self.debug = debug

    
    def connect(self):
        while not self.sta_if.active(True):
            self._debug('Activating')

        stations = []
        self._debug("Getting Station List")
        while not stations:
            stations = self.sta_if.scan()
    
        self._debug(stations)

        self.sta_if.connect(self.ssid_, self.wp2_pass)

        self._debug('waiting to connect to {}'.format(self.ssid_),end=' ')
        while not self.sta_if.isconnected():
            self._debug('.',end='')
            sleep(.05)
    
        self._debug('')
    
        self._debug('connected to {}'.format(self.ssid_))
        
        
    def disconnect(self):
        self.sta_if.active(False)
        self._debug('Deactivating')
        
    def _debug(self,mes,end='\n'):
        if self.debug:
            print(mes,end=end)
