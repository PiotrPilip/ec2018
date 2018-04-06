TABLE_CONTENT = """tweetID TEXT PRIMARY KEY,
   userID TEXT,
   username TEXT,
   location TEXT,
   time_zone TEXT,
   createTime TEXT,
   lang TEXT,
   tweet_text TEXT,
);"""

import sys
sys.path.append('../twitter_api/')
from trackNames import trackNames

for table in trackNames:
    tab = "CREATE TABLE IF NOT EXISTS {} (\n".format(table)
    tab +=TABLE_CONTENT
    print(tab)