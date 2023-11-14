import pickle
import sys
import time

import zmq

import consts
import sentencer

src = consts.S
prt = consts.S_PORT

context = zmq.Context()
push_socket = context.socket(zmq.PUSH)

address = "tcp://" + src + ":" + prt
push_socket.bind(address)

time.sleep(1)

text = sentencer.createText(10, 10)
print(text)

lines = text.splitlines()
for line in lines:
    push_socket.send(pickle.dumps(line))