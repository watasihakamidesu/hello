import zmq
import time

c = zmq.Context(1)
s = c.socket(zmq.REP)
s.bind('tcp://127.0.0.1:1314')
poller = zmq.Poller()
poller.register(s,zmq.POLLIN)
while 1:
    socks = dict(poller.poll(1))
    if s in socks and socks[s] == zmq.POLLIN:
        message = s.recv()
        print(message)
        time.sleep(1)
        s.send(str(time.time()))
