# GitHub Score

By Nick Chinn <nwchinn@gmail.com>


## Overview

This project allows users to enter a github username and it will return info on them along with displaying their rank compared to other users in the DB and will update the D3.js graphic. It uses Flask to display the server-side dynamic pages.

## Virtual Environment (env)

When setting up the project, you should set up a virtual environment to install the Python tools and libraries locally, which won't affect Python tools and libraries elsewhere on your computer.

The folder: *env/* contains all the Python libraries and to create it, run the following command in the project directory: `python3 -m venv env`

**Pitfall**: If you’re on OSX and have previously installed Anaconda, use the full path to the Python executable.
```
$ which python
/Users/nwchinn/anaconda/bin/python
$ rm -rf env  # Remove environment from previous step and start over
$ /usr/local/bin/python3 -m venv env
```

**Pitfall**: If the PYTHONPATH environment variable is set, then this can cause problems. Check this when you first start a new shell.
```
$ echo $PYTHONPATH  # Output isn't blank, problem!
/Users/nwchinn/anaconda/lib/
$ rm -rf env  # Remove environment from previous step and start over
$ unset PYTHONPATH
$ python3 -m venv env
```

Activate virtual environment. You’ll need to do this every time you start a new shell.

`$ source env/bin/activate`

Upgrade the Python tools in your virtual environment:

`$ pip install --upgrade pip setuptools wheel`


## Virtual Env

You should already have a virtual environment installed from the Python virtual environment section. Make sure it’s activated, then install the app into the virtual environment. 

```
$ which pip
/usr/local/bin/pip
$ source env/bin/activate
$ which pip
/home/nwchinn/personal_code/FlaskSqliteTemplate/env/bin/pip
$ pip install -e .
```

## App/DB Commands

The database lives in the file var/appname.sqlite3. The var directory is commonly where the system writes data during the course of its operation.

Activate file in order to be able run the start scripts(ghsrun & ghsdb)
$ chmod +x bin/all

Start app w/ DB
$ ./bin/ghsrun

Create DB
$ ./bin/ghsdb

