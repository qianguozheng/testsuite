#!/usr/bin/env python
#coding=utf-8

import httplib
import urllib

httpClient = None
params = None #POST content

host = None
port = None

#response = None


params = {"Name": "Qian", "Sex": "man"}
method = "POST"
host = "www.yswifi.com"
port = 80
url = "/ysapi/user_auth.php"

class Browser:
    @staticmethod
    def request():
        global params
        global method
        #global response
 
        try:
            print "Test1"
            httpClient = httplib.HTTPConnection(host, port)
            print "Test2"
            #if params and method == "POST":
            hello = urllib.urlencode(params)
            print "Test3"
            #params = urllib.urlencode({'name':'tom', 'age':25})
            #headers = {"Content-Type": 'application/x-www-form-urlencoded',
                       #'Accept':'text/plain'}
                #print "params encoded:" ,hello
            httpClient.request("POST", "/ysapi/rep_userstatus.php")
            print "Test4"
            #response 是HTTPResponse
            response = httpClient.getresponse()
            print response.getheaders()
            print response.status
            print response.reason
            print response.read()
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close() 
    def dynamicmethod(self):
        print "dynamicmethod test"
if __name__ == "__main__":
    Browser.request()
    a = Browser()
    a.dynamicmethod()