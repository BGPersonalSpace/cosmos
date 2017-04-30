## Start github collection

1. Fork https://github.com/variomeproj/cosmos
2. Clone from your forked project to your local
```
$ git clone https://github.com/YourFork/cosmos.git
```
3. Add original project to your local remote
```
$ git remote add upstream git@github.com:variomeproj/cosmos.git
```
4. Branch
Following git-flow (http://nvie.com/posts/a-successful-git-branching-model/), the project have both a master and
a develop branch. The general rule is that if you are bug fixing, then branch from master and if you are adding 
a new feature then branch from develop.
```
$ git checkout master
$ git pull upstream master && git push origin master
$ git checkout -b your-branch-name
```
5. Do your work
6. Push to github
```
$ git push -u origin your-branch-name
```
7. Create PR on github

## Start development

### Set up virtual env

Use python3 virtual environment. After clone the project to local, set up virtual env and install required
packages:

```
$ virtualenv --python=python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Start local server
The project is configured to use MySQL database. Export environments before run local server:

```
$ export DB_HOST=localhost DB_NAME=your_db_name DB_USER=your_db_user DB_PWD=your_db_password
$ python manage.py migrate
$ python manage.py loaddata db.json
$ python manage.py runserver 0.0.0.0:your_port
```
