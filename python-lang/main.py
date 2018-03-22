#! /usr/bin/python

full = list()
function = ['len']
handle = open("sample.txt")
for line in handle:
    line = line.rstrip()
    words = line.split()
    full = full + words
for word in full:
    for item in function:
        if item in word:
            print word
    
