#!/usr/bin/env python2
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
      self.send_header('Access-Control-Allow-Origin', '*')
      SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        if self.path.startswith('/images/'):
            self.path = '/library' + self.path
        if self.path.startswith('/vendor/'):
            self.path = '/library' + self.path
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    BaseHTTPServer.test(CORSRequestHandler, BaseHTTPServer.HTTPServer)

# to run python simple-cors-http-server.py
