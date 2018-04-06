CREATE KEYSPACE IF NOT EXISTS twitter_mdp WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};
USE twitter_mdp
CREATE TABLE metoo(
   tweetID INT PRIMARY KEY,
   userID INT,
   location TEXT,
   time_zone TEXT,
   createTime TEXT,
   lang TEXT,
   tweet_text TEXT,
);
