import subprocess
from configparser import ConfigParser
import sys

cfg = ConfigParser()
cfg.read('../../main.conf')

JOB_TYPES = {'language':'src/hadoop/language/','users':'src/hadoop/users/','neighbor':'src/hadoop/neighbor/' }
JOB_DATA = {'language':'data/language/','users':'data/users/','neighbor':'data/neighbor/'}

sys.path.append('../master_database_pusher')
import mdp_database_queries

def request_hadoop_job(jobname,number,since,keyword):
    path = cfg['MAIN']['path']+JOB_TYPES[jobname]
    mdp_database_queries.select_since(since,keyword,cfg['MAIN']['path']+JOB_DATA[jobname]+'input/in.csv')
    command = ['python3',path+'run_job.py',str(number)]
    subprocess.run(command,cwd=path)


