## start github collection

1. Fork https://github.com/variomeproj/cosmos
2. Clone from your forked project to your local
```
git clone https://github.com/YourFork/cosmos.git
```
3. Add original project to your local remote
```
git remote add upstream git@github.com:variomeproj/cosmos.git
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
git push -u origin your-branch-name
```
7. Create PR on github
