import pickle
import sys
import time

import zmq

import consts

me = str(sys.argv[1])

src = consts.R1 if me == '1' else consts.R2
prt = consts.R1_PORT if me == '1' else consts.R2_PORT

context = zmq.Context()
pull_socket = context.socket(zmq.PULL)

pull_socket.bind("tcp://" + src + ":" + prt)

time.sleep(1)

counters = {x:0 for x in consts.words[int(me)-1::consts.REDUCERS]}

print("{} started".format(me))
print(counters)

while True:
    word = pickle.loads(pull_socket.recv())
    if (word in counters):
        counters[word] += 1
        print(word + " " + str(counters[word]))
    else:
        print("wrong word or wrong counter... we'll never know")
