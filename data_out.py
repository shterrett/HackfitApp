import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import json

ServerClass = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"
OutHandler = SimpleHTTPRequestHandler

def start_server(data):
  write_data(data)
  PORT = 8000
  server_address = ('0.0.0.0', PORT)

  OutHandler.protocol_version = Protocol
  httpd = ServerClass(server_address, OutHandler)

  sa = httpd.socket.getsockname()
  print "Serving HTTP on", sa[0], "port", sa[1], "..."
  httpd.serve_forever()

def write_data(data):
  file = open('index.json', 'w')
  file.write(json.dumps(data))
  file.close()
