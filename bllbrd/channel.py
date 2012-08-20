import requests

from .utils import curry

class Channel(object):
    API_ENDPOINT = 'http://bllbrd.cloud.pb.io/api'
    
    def __init__(self, name):
        self.name = name
    
    def post(self, type, **kwargs):
        payload = dict(type=type, **kwargs)
        r = requests.post('%s/%s' % (self.API_ENDPOINT, self.name), data=payload)
        return r.json
    
    url = curry(post, type='url')
    html = curry(post, type='html')