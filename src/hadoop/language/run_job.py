import subprocess
from configparser import ConfigParser
import sys

cfg = ConfigParser()
cfg.read('../../../main.conf')

data_path='/home/piotr/hackathon/ec-challenge-2018/data/language/'
number=sys.argv[1]

command = [
    cfg['HADOOP']['hadoop_path'],
    'jar',
    cfg['HADOOP']['streamer_path'],
    '-mapper', 'mapper.py',
    '-reducer', 'reducer.py',
    '-input', data_path+'/input/*',
    '-output', data_path+'/output'+str(number)
]
print(command)
subprocess.run(command)