#!/bin/bash
data_path=/home/piotr/hackathon/ec-challenge-2018/data/users/

/usr/local/hadoop/bin/hadoop jar \
 /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.5.jar \
 -mapper "mapper.py" \
 -reducer "reducer.py"\
 -input "$data_path""input/*" \
 -output "$data_path"$1

