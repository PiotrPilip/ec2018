TABLE_CONTENT = """tweetID TEXT PRIMARY KEY,
   userID BIGINT,
   username BIGINT,
   location TEXT,
   time_zone TEXT,
   createTime BIGINT,
   lang TEXT,
   tweet_text TEXT,
);"""

from cassandra.cluster import Cluster
import sys
sys.path.append('../twitter_api/')
from trackNames import trackNames
from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('../../main.conf')

for table in trackNames:
    cluster = Cluster()
    session = cluster.connect(cfg["DATABASE"]['keyspace_md'])
    tab = "CREATE TABLE IF NOT EXISTS {} (\n".format(table)
    tab +=TABLE_CONTENT
