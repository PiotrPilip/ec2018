#!/usr/bin/python3
import sys
import csv

#configuable!
USER_INDEX = 7


reader = csv.reader(sys.stdin)
for row in reader:
    print("%s;%s" % (row[USER_INDEX],1))
