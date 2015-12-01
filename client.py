import zmq
import random
import sys
import time

port = "5557"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while True:
    msg = socket.recv()
    print msg
    message = raw_input("Enter : ")
    socket.send("client : " + message)
    # socket.send("client message to server1")
    # socket.send("client message to server2")
    time.sleep(1)
