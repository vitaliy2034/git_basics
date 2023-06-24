#!/usr/bin/env python3

"""Calculate deposit percent yield based on time period.

Imagine your friend wants to put money on a deposit.
He has got many offers from different banks:
- First bank declares +A% each day;
- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;
- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...

Your friend gets a terrible headache calculating all this stuff,
and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.

Let's implement this.

A simplified task:
Given the SUM amount of money, and PERCENT yield promised in a
FIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.

Math formula:
p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))
"""


# TODO: add lines to calculate yields for some common periods
#       of time (e.g. 1 month, 1 year, 5 years, 10 years)
# TODO: change the script to output the 1-year percent yield
#       as well
# TODO: (extra) Output only percents if the initial SUM is
#       not known at the moment the script is run


USAGE = """USAGE: {script} [initial_sum] percent fixed_period set_period

\tCalculate deposit yield. See script source for more details.
\tIf initial_sum is not provided, it will output only the yield percent.
"""
USAGE = USAGE.strip()


def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    growth = (1 + per) ** (set_period / fixed_period)
    return growth


def main(args):
    """Gets called when run as a script."""

    if len(args) < 3 + 1 or len(args) > 4 + 1:
        exit(USAGE.format(script=args[0]))

    # If only 3 arguments are provided, initial_sum is set to 0
    initial_sum = 0 if len(args) == 3 + 1 else float(args[1])

    percent, fixed_period, set_period = map(float, args[-3:])

    # Creating a dictionary mapping period names to their values in years
    periods = {
        '1-month': 1/12,
        '1-year': 1,
        '5-year': 5,
        '10-year': 10,
        f'{set_period}-year': set_period,
    }

    # For each period, calculate the growth and yield and print them
    for name, period in periods.items():
        growth = deposit(initial_sum, percent, fixed_period, period)
        yield_ = initial_sum * growth
        print(f'{name} yield: {yield_:.2f}, in percentage +{growth - 1:.0%}')


if __name__ == '__main__':
    import sys

    main(sys.argv)
