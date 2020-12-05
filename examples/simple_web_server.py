# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except ImportError:
  import socket

import network

import esp
esp.osdebug(None)

#import gc
#gc.collect()

ssid = 'MicroPython-AP'
password = '1234567891'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())


def web_page():
  html = """<html><head><title>Hi There</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
    </html>

"""

  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  response = web_page()
  conn.sendall(response)
  conn.close()