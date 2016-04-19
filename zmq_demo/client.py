import zmq
import time


c = zmq.Context()
s = c.socket(zmq.REQ)
s.connect('tcp://127.0.0.1:1314')
for i in range(50):
    s.send("hello")
    msg = s.recv()
    print i, msg
    time.sleep(1)
