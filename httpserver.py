"""
    HTTP Request Sample
    
    GET /us/r1000/149/Purple5/v4/49/ae/fc/49aefcdd-6793-a67b-68b7-604af624c42a/xyh1316843107459888545.D2.pd.ipa?source=a366.phobos.apple.com HTTP/1.1
Host: 192.168.111.147:51564
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
Cookie: downloadKey=expires=1435829830~access=/us/r1000/149/Purple5/v4/49/ae/fc/49aefcdd-6793-a67b-68b7-604af624c42a/xyh1316843107459888545.D2.pd.ipa*~md5=faddb039f40122fd88776b8711a51e0b
iCloud-DSID: 1349926139

HTTP/1.1 200 OK
Content-Type: text/plain
X-Akamai-Request-ID: 2ba08b73
X-Cache: HIT from cache.51cdn.com
Via: 1.0 fzh182:8080 (Cdn Cache Server V2.0), 1.0 dhzh22:5706 (Cdn Cache Server V2.0)
Server: Apache
X-Apple-Cache-Session: CdUFGYcsPmd9
Date: Tue, 30 Jun 2015 03:37:12 GMT
Content-Length: 11091400
Connection: keep-alive
Etag: "aab3c644a80e8ac8205e8152b1535589:1435338253"
Accept-Ranges: bytes
Last-Modified: Fri, 26 Jun 2015 17:04:09 GMT
"""
import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
			#if self.path.endswith(".html")
			self.send_response(200)
			self.send_header('Content-Type','text/plain')
			self.send_header('X-Akamai-Request-ID','2ba08b73')
			self.send_header('X-Cache','HIT from cache.51cdn.com')
			self.send_header('Via','1.0 fzh182:8080 (Cdn Cache Server V2.0), 1.0 dhzh22:5706 (Cdn Cache Server V2.0)')
			self.send_header('Server','Apache')
			self.send_header('X-Apple-Cache-Session','CdUFGYcsPmd9')#Date no print
			self.send_header('Content-Length','11091400')
			self.send_header('Connection','keep-alive')
			#self.send_header('Content-Type','text/plain')
			#self.send_header('Content-Type','text/plain')
			self.send_header('Etag','\"aab3c644a80e8ac8205e8152b1535589:1435338253\"')
			self.send_header('Accept-Ranges','bytes')
			self.send_header('Content-Type','text/plain')#last-Modified

			self.end_headers()
#write file
			f = open("./0");
			self.wfile.write(f.read())
			f.close()
			return

def main():
	try:
		server = HTTPServer(('', 8000), MyHandler)
		print 'started httpserver...'
		server.serve_forever()
	except KeyboardInterrupt:
		print '^C received, shutting down server'
		server.socket.close()

if __name__ == '__main__':
	main()
