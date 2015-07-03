import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.1"

if sys.argv[1:]:
	port = int(sys.argv[1])
else:
	port = 8000

server_address = ('192.168.111.147', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)
sa = httpd.socket.getsockname()
print 'Serving HTTP on', sa[0], "port", sa[1], "..."
httpd.serve_forever()
