# connection_manager.py
"""Provide a class to handle interaction with the web
    There seems to be a problem with https sites that
    causes a memory overflow.
    
    After a few https gets the device resets.
    
    https seems to work Ok in the main thread, so if you want a secure
    connection do it in the main thread, not here.

"""

import time
try:
    import requests
except ImportError:
    import urequests as requests

import threading
 
class ConnectionManager:
    def __init__(self):
        self._terminate = False
        self._my_thread = None
        self._put_list = []
        self._get_list = []
        self.response_list = []
        
    def add(self,mode,url,data=None,UID=None):
        # Add an item to the put or get lists
        req_dict = self._default_response()
        req_dict['url'] = url
        req_dict['UID'] = UID
        if mode.lower() == 'put':
            req_dict['data'] = data if data else ''
            self._put_list.append(req_dict)
        else:
            # must be a get
            self._get_list.append(req_dict)
            
    def __exit__(self):
        self.stop()
        while self.working:
            time.sleep(.5)
            
        return
        
    def start(self):
        # create a thread and start it
        if not self._my_thread:
            self._my_thread = threading.Thread(group=None,target=self._manager)
            self._my_thread.start()
            
            
    def stop(self):
        self._terminate = True


    def _manager(self):
        # manage the get and put queues
        while self.working or not self._terminate:
            if self._get_list:
                req = self._get_list[0]
                url = req['url']
                UID = req['UID'] # so posting method can find their response if needed
                try:
                    response = requests.get(url)
                    self.set_response(url,response,UID=UID)
                    
                    print("Read {content} bytes from {url}".format(content=len(response.content),url=url))
                except Exception as e:
                    print('Got Exception "{}" while processing {}'.format(str(e),url))
                    return # end the thread
                self._get_list.pop()
                
            if self._put_list:
                req = self._put_list[0]
                url = req['url']
                data = req['data']
                UID = req['UID'] # so posting method can find their response if needed
                try:
                    response = requests.put(url,data)
                    self.set_response(url,response,UID=UID)
                   
                    print("Got {content} bytes from {url}".format(content=len(response.content),url=url))
                except Exception as e:
                    print('Got Exception "{}" while processing {}'.format(str(e),url))
                    
                self._put_list.pop()
        
        return self.__exit__() # end the thread
        
        
                
    def set_response(self,url,response,UID=None):
        # without a UID, there is no good way to get the
        #  correct response, so only save responsed we can find
        if UID:
            response_dict = self._default_response()
            response_dict.update({'url':url,'response':response,})
            response_dict.update({'UID':UID})
            # Should probobly check that there is heep space for this first...
            self.response_list.append(response_dict)
            
        
    @property
    def working(self):
        return True if self._get_list or self._put_list else False


    def _default_response(self):
        return {
            'url':None,
            'response':None,
            'data':None,
            'UID':None,
            }

        
