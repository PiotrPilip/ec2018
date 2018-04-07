#!/usr/bin/python3
import sys
import csv

#configuable!
LANG_INDEX = 2


reader = csv.reader(sys.stdin)
for row in reader:
    print("%s;%s" % (row[LANG_INDEX],1))
