# pip on Micropython

To pip packages into the micropython device use upip.

upip.help() says:

```
    upip - Simple PyPI package manager for MicroPython
    Usage: micropython -m upip install [-p <path>] <package>... | -r <requirements.txt>
    import upip; upip.install(package_or_list, [<path>])

    If <path> is not given, packages will be installed into sys.path[1]
    (can be set from MICROPYPATH environment variable, if current system
    supports that).
    Current value of sys.path[1]: /lib

    Note: only MicroPython packages (usually, named micropython-*) are supported
    for installation, upip does not support arbitrary code in setup.py.
```


## some interesting packages on PyPi:

    * pip install micropython-wifimanager
    
        Use a json file to store credentials for wifi stations to try and also
        create a base station on the device
        
    * pip install micropython-hmac
    
    * pip install micropython-ssd1306
    
        Use the ssd1306 OLED display
        
    * pip install micropython-mqtt
    
        MQTT Client
        
    * pip install micropython-ulogging
    
    * pip install micropython-random
    
        dummy for random
        
    