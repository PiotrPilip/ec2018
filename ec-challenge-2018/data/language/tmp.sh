#!/bin/bash
/usr/local/hadoop/bin/hadoop jar \
 /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.5.jar \
  -mapper /home/piotr/hackathon/ec-challenge-2018/src/hadoop/language/mapper.py   -reducer /home/piotr/hackathon/ec-challenge-2018/src/hadoop/language/reducer.py -input input/* -output output1

