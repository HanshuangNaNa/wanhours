#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2018年02月26日 星期一 21时39分50秒
# File Name: base.py
# Description:
"""
import logging
import BaseHTTPServer

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    Page = '''\
            <html>
            <body>
            <p>Hello,web!</p>
            </body>
            </html>
            '''

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type','text/html')
        self.send_header('Content-Length',str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page)

if __name__ == '__main__':
    serverAddress = ('',8080)
    server = BaseHTTPServer.HTTPServer(serverAddress,RequestHandler)
    server.serve_forever()
