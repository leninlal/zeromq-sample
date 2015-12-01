import zmq
import random
import sys
import time

port = "5557"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:
    # socket.send("Server message to client3")
    message = raw_input("Enter : ")
    socket.send("server : " + message)
    msg = socket.recv()
    print msg
    time.sleep(1)
