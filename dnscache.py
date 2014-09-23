
import socket
_dnscache={}
def _setDNSCache():
    """
    Makes a cached version of socket._getaddrinfo to avoid subsequent DNS requests.
    """
    def _getaddrinfo(*args, **kwargs):
            global _dnscache
            if args in _dnscache:
                print str(args) + " in cache"
                return _dnscache[args]
            else:
                print str(args) + " not in cache"
                _dnscache[args] = socket._getaddrinfo(*args, **kwargs)
                return _dnscache[args]
    if not hasattr(socket, '_getaddrinfo'):
        socket._getaddrinfo = socket.getaddrinfo
        socket.getaddrinfo = _getaddrinfo

def test():
    _setDNSCache()
    import urllib
    urllib.urlopen('http://www.baidu.com')
    urllib.urlopen('http://www.baidu.com')

test()