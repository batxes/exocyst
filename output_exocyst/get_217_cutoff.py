#!/usr/bin/python

#script go get the cutoff imp score for the first n best scores
import numpy as np
import re

path = "/home/bioinfo/exocystimp/output_1_y2h_definitive/scores_final.txt"
f= open(path,'r')

scores = []

for line in f:
    if '####' in line:
        break
    if '\t' in line:
        values = re.split ('\t',line)
        scores.append(values[1])
    
scores.sort()
print len(scores)
print scores[216]
print scores[217]
print scores[299]
print scores[300]
