#!/usr/bin/python 
'''
Simple Banner Grabbing by santosopuguh
'''
import socket as sc

class BannerGrab():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.result = ''
    
    def getBanner(self):
        sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        try:   
            sock.connect((self.ip, self.port))
            self.result = sock.recv(1024)
            sock.close()
            print 'Result:', self.result
        except Exception, e:
            print 'Something\'s wrong with %s:%d \nException type is %s' % (self.ip, self.port, `e`)

if __name__ == '__main__':
    ip = raw_input('Target IP Address: ')
    port = raw_input('Port Number: ')
    objBan = BannerGrab(ip, int(port));
    objBan.getBanner()