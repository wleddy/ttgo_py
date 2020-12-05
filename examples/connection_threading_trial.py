# connection_threading_trial.py
"""Test out my connection manager class"""

import time
 
# Open a wifi connection
try:
    import open_wallace
except ImportError:
    pass #not needed on connected computer

from count_o_rama.connection_manager import ConnectionManager

        
        
tricky_sites = [
    "https://www.jython.org",
    "http://olympus.realpython.org/dice",
]
easy_sites = [
    "http://olympus.realpython.org/dice",
]

sites_to_use = easy_sites
UID = 'test'

conn = ConnectionManager()
conn.start()

def add_gets(sites):
    for site in sites:
        conn.add('get',site,UID=UID)

def add_puts(puts):
    for site in puts:
        put_dict = conn._default_response()
        put_dict['url'] = site['url']
        put_dict['data'] = site['data'] if site['data'] else ''
        put_dict['UID'] = site['UID'] if site['UID'] else ''
        conn.add('put',put_dict)

print('Waiting for first sites list')
# download_sites()
for x in range(3):
    print("pause1",x)
    time.sleep(1)


print('Beginning first Downloads')
# download_sites()
add_gets(sites_to_use.copy() * 1)

for x in range(3):
    print("pause2",x)
    time.sleep(1)
    
print('Begin second downloads')
add_gets(sites_to_use.copy() * 10)

#Appending values to sites works atomically! Yeah!!!

conn.stop() # Won't exit while still working

# this keeps the main alive till the manager is done
print('Wait for work to finish before Exiting main ')
while conn.working:
    time.sleep(.5)

print('Exiting main')
    
for resp in conn.response_list:
    print('resp: {}, len: {}, UID: {}'.format(
            resp['response'].content[0:10].decode().replace('\r',' ').replace('\n',''),
            len(resp['response'].content),
            resp['UID'],
            resp['data'],
            )
        )
