#!/usr/bin/env python3

import sys
import atexit
import datetime

def save(heatmap, starttime):
    with open(str(starttime), "w") as f:
        f.write("start: %s\n"% starttime)
        f.write("end: %s\n"% datetime.datetime.now())
        total = 0
        for key in heatmap:
            f.write("key %s: %d\n"%(key, heatmap[key]))
            total += heatmap[key]

        f.write("total: %d\n"%total)


heatmap = dict()
start = datetime.datetime.now()

atexit.register(save, heatmap, start)

total = 0
for line in sys.stdin:
    if "key press" in line: 
        key_id = line.split("press")[1].strip()
        total += 1
        try:
            heatmap[key_id] +=1
        except KeyError:
            heatmap[key_id] = 1
        print (total)
