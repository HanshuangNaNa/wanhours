#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: HansHuang
# Created Time : 2018年01月24日 星期三 21时23分06秒
# File Name: demo.py
# Description:
"""
import logging
import socket
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s : %(levelname)s %(message)s',datefmt='%Y-%m-%d %A %H:%M:%S')

def fetch(url):
    sock = socket.socket()
    sock.connect(('xkcd.com',80))
    request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(url)
    #发送TCP数据
    sock.send(request.encode('ascii'))
    response = b''
    #接收最大数据量是4096
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)
    links = parse_links(response)
    q.add(links)

def demo(url):
    pass

if __name__ == '__main__':
    pass
