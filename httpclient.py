#!/usr/bin/env python
#coding=utf-8

"""
GET /a366.phobos.apple.com/us/r1000/149/Purple5/v4/49/ae/fc/49aefcdd-6793-a67b-68b7-604af624c42a/xyh1316843107459888545.D2.pd.ipa?wsiphost=local HTTP/1.1
Host: 125.90.204.110
Accept: */*
X-Apple-Store-Front: 143465-19,26 ab:SIM0
X-Apple-Partner: origin.0
Accept-Encoding: gzip, deflate
Accept-Language: zh-cn
X-Apple-Client-Versions: iTunesU/2.1.1; GameCenter/2.0
X-Apple-Connection-Type: WiFi
User-Agent: itunesstored/1.0 iOS/8.3 model/iPhone6,2 build/12F70 (6; dt:90)
Connection: keep-alive
X-Dsid: 1349926139
Cookie: downloadKey=expires=1436520944~access=/us/r1000/149/Purple5/v4/49/ae/fc/49aefcdd-6793-a67b-68b7-604af624c42a/xyh1316843107459888545.D2.pd.ipa*~md5=87a24bab8d84af2f80578836544dae84
iCloud-DSID: 1349926139
"""
import httplib
import urllib

httpClient = None

params = None
def GET():
        headers = {	"Host":"125.90.204.110", 
			"Accept":"*/*", 
			"X-Apple-Store-Front":"143465-19,26 ab:SIM0",
			"X-Apple-Partner": "origin.0",
			"Accept-Encoding": "gzip, deflate",
			"Accept-Language": "zh-cn",
			"X-Apple-Client-Versions": "iTunesU/2.1.1; GameCenter/2.0",
			"X-Apple-Connection-Type": "WiFi",
			"User-Agent": "itunesstored/1.0 iOS/8.3 model/iPhone6,2 build/12F70 (6; dt:90)",
			"Connection": "keep-alive",
			"X-Dsid": "1349926139",
			"Cookie": "downloadKey=expires=1436520944~access=/us/r1000/149/Purple5/v4/49/ae/fc/49aefcdd-6793-a67b-68b7-604af624c42a/xyh1316843107459888545.D2.pd.ipa*~md5=87a24bab8d84af2f80578836544dae84",
			"iCloud-DSID": "1349926139"
		}
        try:
                httpClient = httplib.HTTPConnection("14.215.9.17", 80)
                httpClient.request("GET", "/a573.phobos.apple.com/us/r1000/123/Purple1/v4/99/4a/76/994a76dd-0efa-2443-c03b-5f7165ed5999/dub8500894790411176606.D2.dpkg.ipa?wsiphost=local", params, headers)

                #response 是HTTPResponse
                response = httpClient.getresponse()
                print response.getheaders()
                print response.status
                print response.reason
                response.read()
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
