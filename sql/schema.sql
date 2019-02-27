CREATE TABLE users(
  login VARCHAR(20) NOT NULL,
  gid INTEGER,
  name VARCHAR(40),
  email VARCHAR(40),
  followers INTEGER,
  following INTEGER,
  public_repos INTEGER,
  public_gists INTEGER,
  stars INTEGER,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  repos_url VARCHAR(200),
  PRIMARY KEY(login)
);

CREATE TABLE urls(
  login PRIMARY KEY,
  url VARCHAR(200),
  html_url VARCHAR(200),
  followers_url VARCHAR(200),
  following_urlVARCHAR(200),
  gists_url VARCHAR(200),
  starred_url VARCHAR(200),
  subscriptions_url VARCHAR(200),
  organizations_url VARCHAR(200),
  repos_url VARCHAR(200),
  events_url VARCHAR(200),
  received_events_url VARCHAR(200)
)