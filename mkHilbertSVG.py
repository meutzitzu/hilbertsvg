#!/usr/bin/python3
import math
FILE = open("hilbert.svg", "w")

SIZE    = 128
LEVEL   = 5

SEED = [(0,0),(0,1),(1,1),(1,0)]
PATH = SEED
def hamilton(path):
    newpath=[]
    for q in SEED:
        for p in path:
            newpath.append((p[0] + math.sqrt(len(path))*SEED[(SEED.index(q)) % len(SEED)][0], p[1] + math.sqrt(len(path))*SEED[(SEED.index(q)) % len(SEED)][1]))
    return newpath

dstring=[]


for k in range(0, LEVEL):
    lstring= ""
    for p in PATH:
        lstring+="L %d %d " % (SIZE * p[0] / pow(2,LEVEL), SIZE * p[1] / pow(2,LEVEL))
    lstring = lstring.replace('L', 'M', 1)
    dstring.append(lstring)
    PATH = hamilton(PATH);

print(dstring)
svgstring = "<svg xmlns=\"http://www.w3.org/2000/svg\" viewbox=\"%d %d\" style=\"background-color:#000; margin: 1em;\">\n<path d=\"%s\" stroke=\"yellow\" stroke-width=\"1px\" fill=\"none\"/>\n</svg>" % (SIZE, SIZE, dstring[LEVEL-1])
FILE.write(svgstring)
