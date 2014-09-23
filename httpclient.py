#!/usr/bin/env python
#coding=utf-8

import httplib
import urllib

httpClient = None

params = None
def GET():
        headers = {"Host":"gw.apfree.net", "Accept":"text/html"}
        try:
                httpClient = httplib.HTTPConnection("gw.apfree.net", 80)
                httpClient.request("GET", "/index_ad.php/ad_show/show/apfree?dev_id=3c8f4cbe24aa0a9907d88fd36d7ce1ba&gw_address=192.168.0.1&gw_port=2060&url=http%3A//www.ibook.info/acFM7VheBFYXeD/ZhL4B8FbXWK6Xr/rfMJDdI0rOArS4.html&mac=30:10:e4:8b:a3:c7", params, headers)

                #response 是HTTPResponse
                response = httpClient.getresponse()
                print response.getheaders()
                print response.status
                print response.reason
                print response.read()
                print response.getheaders()
                print response.getheader('location')

        except Exception, e:
                print e
        finally:
                if httpClient:
                        httpClient.close()


def POST():
        try:
            params = urllib.urlencode({'name':'tom', 'age':25})
            headers = {"Content-Type": 'application/x-www-form-urlencoded',
                       'Accept':'text/plain'}
            httpClient = httplib.HTTPConnection("www.baidu.com", 80, timeout=30)
            httpClient.request("POST", "/test.php", params, headers)

            response= httpClient.getresponse()
            print response.status
            print response.reason
            print response.read()
            print response.getheaders()
            print response.getheader('location')
        except Exception, e:
                print e
        finally:
                if httpClient:
                        httpClient.close()

GET()
