#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import datetime

port = 8091

class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
       
       if self.path == '/c':
            
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write("This is app_two - c !")

        elif self.path == '/d':
            
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write("This is app_two - d !")

    

server = HTTPServer(('', port), myHandler)
server.serve_forever()
