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
  PRIMARY KEY(login)
);