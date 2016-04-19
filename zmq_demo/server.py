import zmq
import time


c = zmq.Context(1)
s = c.socket(zmq.REP)
s.bind('tcp://127.0.0.1:1314')
while 1:
    msg = s.recv()
    print msg
    s.send("form serv1")
    time.sleep(1)
