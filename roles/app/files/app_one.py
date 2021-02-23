#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import datetime

port = 8091

class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/a':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write("<b> This is app_one - a !</b>")
        elif self.path == '/b':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write("<b> This is app_one - b !</b>")

    

server = HTTPServer(('', port), myHandler)
server.serve_forever()
