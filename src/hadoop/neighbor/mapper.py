#!/usr/bin/python3
import sys
import csv

#configuable!
TEXT_INDEX = 5


reader = csv.reader(sys.stdin)
for row in reader:
    text = row[TEXT_INDEX]
    text = text.split(' ')
    for word in text:
        print("%s;%s" % (text,1))
