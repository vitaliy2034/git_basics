### Merge result
```
touch README.MD
git add README.MD
git commit -m "Readme changed."

mkdir git_basics
git init
```

### Subtask 3
```
git checkout -b first_branch
git status
git commit -a -m "Readme changed. Added commands that solves 1st subtask."
```

### Subtask 4
```
git checkout master
git commit -a -m "Readme changed. Added commands that solves 2nd subtask."
git log --all --decorate --oneline --graph
```
