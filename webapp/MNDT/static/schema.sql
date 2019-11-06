DROP TABLE IF EXISTS test;
DROP TABLE IF EXISTS earthquake;

CREATE TABLE test(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tweet_text TEXT NOT NULL,
  post_time TIMESTAMP NOT NULL,
  origin_long FLOAT NOT NULL,
  origin_lat FLOAT NOT NULL,
  latitude FLOAT NOT NULL,
  longitude FLOAT NOT NULL,
  predicted_relevant BOOLEAN
);

CREATE TABLE earthquake(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  latitude FLOAT NOT NULL,
  longitude FLOAT NOT NULL
);
