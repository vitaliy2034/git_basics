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

# 02ex01-deposits.py

### Usage

```
python3 02ex01-deposits.py [initial_sum] percent fixed_period set_period
```

Parameters:

- initial_sum: (optional) Initial amount of the deposit. If not provided, the script will output only the yield percent.
- percent: Annual interest rate as a percentage (e.g., 5 for 5%).
- fixed_period: Period for which the interest rate is fixed (usually 1 year).
- set_period: Desired period for which to calculate the yield.

### Example:

```
python3 02ex01-deposits.py 1000 5 1 2
```

This command calculates the yields of a deposit of $1000 with a fixed annual interest rate of 5% for 1 month, 1 year, 5 years, 10 years, and 2 years.

# 02ex02-vikings.py

### Usage

```
python3 02ex02-vikings.py [num_dishes] --menu [menu]
```

Parameters:

- num_dishes: (optional) Number of dishes in the menu. Default: 8.
- --menu: (optional) List of dishes to be included in the menu. Default: ['spam', 'egg', 'sausage', 'bacon'].

### Example:

```
python3 02ex02-vikings.py 10 --menu soup salad steak
```

# task02_tool.py

### Usage

```
python3 task02_tool.py [length] [complexity]
```

Parameters:

- length: Length of the password to be generated.
- complexity: Complexity level (1 to 4) for the password.

### Example:

```
python3 task02_tool.py 12 4
```

This will generate a password like kD3$9nB&1Pc$.
