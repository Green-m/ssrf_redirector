#!/usr/bin/env python3

#python3 ./redirector.py 8000 http://127.0.0.1/

import sys
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

if len(sys.argv)-1 != 2:
    print("Usage: {} <port_number> <url>".format(sys.argv[0]))
    sys.exit()

class Redirect(BaseHTTPRequestHandler):
    def redirector_header(self, header_value):
        return header_value if  header_value else sys.argv[2]

    def do_HEAD(self):
        #logging.error(self.headers)
        print(self.headers)
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        #logging.error(self.headers)
        print(self.headers)
        location_url = self.redirector_header(self.headers.get('loc'))
        self.send_response(302)
        self.send_header('Location', location_url)
        self.end_headers()

    def do_POST(self):
        #logging.error(self.headers)
        #logging.error(self.rfile.read(int(self.headers.getheader('Content-Length'))))
        print(self.headers)
        if self.headers.get('Content-Length'):
            print(self.rfile.read(int(self.headers.get('Content-Length'))))
        location_url = self.redirector_header(self.headers.get('loc'))
        self.send_response(307)
        self.send_header('Location', location_url)
        self.end_headers()




HTTPServer(("", int(sys.argv[1])), Redirect).serve_forever()
