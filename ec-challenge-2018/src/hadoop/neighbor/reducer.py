#!/usr/bin/python3
import sys

current_word=None
word_count=0
word =None


for line in sys.stdin:
   line=line.strip()
   try:
      word, count = line.split(';')
   except ValueError:
      continue
   try:
      count = int(count)
   except ValueError:
      continue
   if current_word == word:
      current_count += count
   else:
      if current_word:
         print( '%s;%s' % (current_word, current_count))
      current_count = count
      current_word = word
if current_word == word:
   print('%s;%s' % (current_word, current_count))
