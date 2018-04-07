CREATE KEYSPACE IF NOT EXISTS twitter_mdp WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};
USE twitter_mdp;
CREATE TABLE IF NOT EXISTS china(
   tweetID BIGINT,
   userID BIGINT,
   username TEXT,
   location TEXT,
   time_zone TEXT,
   createTime BIGINT,
   lang TEXT,
   tweet_text TEXT,
   PRIMARY KEY(tweetID,createTime)
);
