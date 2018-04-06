CREATE KEYSPACE IF NOT EXISTS twitter_mdp WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};
USE twitter_mdp;
CREATE TABLE IF NOT EXISTS metoo(
   tweetID TEXT PRIMARY KEY,
   userID TEXT,
   username TEXT,
   location TEXT,
   time_zone TEXT,
   createTime TEXT,
   lang TEXT,
   tweet_text TEXT,
);
CREATE TABLE IF NOT EXISTS china(
   tweetID BIGINT PRIMARY KEY,
   userID BIGINT,
   username TEXT,
   location TEXT,
   time_zone TEXT,
   createTime BIGINT,
   lang TEXT,
   tweet_text TEXT,
);
