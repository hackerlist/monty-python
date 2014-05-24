#-*- coding: utf-8 -*-

"""
    monty.py
    ~~~~~~~~
    Python API Bindings for the Monty server monitoring Go library

    :authors Hackerlist
    :license Apache 2
"""

import requests
from functools import partial
from simplejson import JSONDecodeError

NO_JSON_ERR = lambda url: "Failed to fetch json for: %s" % url

def fmt_err(e, msg=NO_JSON_ERR, data=''):
    return "%s\n\n%s\n%s\n\n%s" % (e, msg, "=" * len(msg), data)

class Monty:
    
    routes = ["status", "nodes", "probes", "scripts", "results"]
    
    def __init__(self, url, version=1, token=None):

        def http_request(url, method, route, id_='', **kwargs):
            url = '%s/api/%s/%s' % (url, route, id_)
            request = getattr(requests, method, requests.get)
            r = request(url, **kwargs)
            try:
                return r.json()
            except JSONDecodeError as e:
                raise ValueError(fmt_err(e, msg=NO_JSON_ERR(url), data=r.content))

        for route in self.routes:
            setattr(self, route, partial(http_request, url, 'get', route))
            attrs = dict((method, partial(http_request, url, method, route))
                         for method in ['get', 'post'])
            cls = type(route.capitalize(), (object,), attrs)
            setattr(self, route.capitalize(), cls)

if __name__ == "__main__":
    m = Monty('http://monty.criticalpha.se',
              token='u1d8jd93rq3o4r32zk432hhg23ihd7s4k35h')
