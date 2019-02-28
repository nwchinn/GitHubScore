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

CREATE TABLE repos(
  repoid INTEGER PRIMARY KEY AUTOINCREMENT,
  rlogin VARCHAR(20) NOT NULL,
  name VARCHAR(100) NOT NULL,
  full_name VARCHAR(150) NOT NULL,
  url VARCHAR(200) NOT NULL,
  html_url VARCHAR(200),
  size INTEGER,
  stargazers_count INTEGER,
  watchers_count INTEGER,
  forks_count INTEGER,
  language VARCHAR(20),
  FOREIGN KEY(rlogin) REFERENCES users(login) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE urls(
  login PRIMARY KEY,
  url VARCHAR(200),
  html_url VARCHAR(200),
  followers_url VARCHAR(200),
  following_url VARCHAR(200),
  gists_url VARCHAR(200),
  starred_url VARCHAR(200),
  subscriptions_url VARCHAR(200),
  organizations_url VARCHAR(200),
  repos_url VARCHAR(200),
  events_url VARCHAR(200),
  received_events_url VARCHAR(200)
);