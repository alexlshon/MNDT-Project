DROP TABLE IF EXISTS posts;

CREATE TABLE posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  post_time TIMESTAMP NOT NULL,
  tweet_text TEXT NOT NULL,
  origin_long FLOAT NOT NULL,
  origin_lat FLOAT NOT NULL,
  latitude FLOAT NOT NULL,
  longitude FLOAT NOT NULL,
  predicted_relevant BOOLEAN
);
