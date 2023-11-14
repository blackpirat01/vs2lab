import random

import consts

words = consts.words

#max words per line
def createText(max_wpl, max_linecount):
    lc = random.randint(1, max_linecount)
    txt = ""
    for i in range(lc):
        txt += createLine(max_wpl)
    return txt

def createLine(max_wordcount):
    wc = random.randint(1, max_wordcount)
    line = ""
    for i in range(wc):
        line += random.choice(words) + " "
    line += "\n"
    return line