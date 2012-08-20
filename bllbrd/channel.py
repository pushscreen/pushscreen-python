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
    
    def url(self, url, **kwargs):
        return self.post(type='url', url=url, **kwargs)
    
    def html(self, html, **kwargs):
        return self.post(type='html', html=html, **kwargs)
    
    def clear(self, **kwargs):
        return self.post(type='clear', **kwargs)
