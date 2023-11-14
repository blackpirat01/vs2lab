import pickle
import sys
import time

import zmq

import consts

red1_addr = "tcp://" + consts.R1 + ":" + consts.R1_PORT
red2_addr = "tcp://" + consts.R2 + ":" + consts.R2_PORT
split_addr = "tcp://" + consts.S + ":" + consts.S_PORT

context = zmq.Context()
pull_socket = context.socket(zmq.PULL)
pull_socket.connect(split_addr)

push_socket1 = context.socket(zmq.PUSH)
push_socket1.connect(red1_addr)
push_socket2 = context.socket(zmq.PUSH)
push_socket2.connect(red2_addr)

time.sleep(1)

while True:
    work = pickle.loads(pull_socket.recv())
    words = work.split()
    for word in words:
        rid = consts.words.index(word) % consts.REDUCERS
        if (rid == 0):
            push_socket1.send(pickle.dumps(word))
        elif (rid == 1):
            push_socket2.send(pickle.dumps(word))
        else:
            print("something went wrong.");