#!/usr/bin/env python3

"""The famous Vikings restaurant from the Monthy Python sketch.

See the sketch origins video first:
https://www.youtube.com/watch?v=zLih-WQwBSc
"""

import random
import argparse

DEF_CHOICE = 8
MENU = ['spam', 'egg', 'sausage', 'bacon']
MENU_MULTI = MENU + ['eggs', 'sausages']
JOINTS = [', and ', ', ', ' and ', ' with ', ' and double portion of ']
PREFERED = MENU[0]
FORBIDDEN = {'not', 'without', 'no'}

SONG = ', '.join([PREFERED.capitalize()] + [PREFERED] * DEF_CHOICE) + '!'

D_WELCOME = ('Welcome to the Vikings restaurant.\n'
             'What would you like to eat?')
D_CHOICE = '> '
D_PROMOTE = "We highly recommend {dishes}" + f', and {PREFERED}...'
D_GOOD = "That's a perfect choice. Let's have more {dishes}" + f', and {PREFERED}!'
D_BAD = "Disgusting. Who eats {dishes}?"
D_UNAVAILABLE = "That's not on our menu.\nWe have {dishes}."


def dialog(num_choice=DEF_CHOICE, menu=MENU):
    """User dialog logic."""
    print(D_WELCOME)
    entry = input(D_CHOICE).strip()
    words = entry.lower().split()
    # Here we change MENU_MULTI to our custom menu and make it lower-case for comparison
    menu_multi_lower = [dish.lower() for dish in menu + [dish + 's' for dish in menu]]

    def promote():
        print(D_PROMOTE.format(dishes=get_dishes(num_choice, menu)))

    if set(words) & set(menu_multi_lower):  # And here we compare with our updated menu
        if set(words) & set(FORBIDDEN):
            print(D_BAD.format(dishes=entry))
            promote()
        else:
            print(D_GOOD.format(dishes=entry))
            print(f'Vikings: "{SONG}"')
        return

    if not words:
        promote()
        return

    print(D_UNAVAILABLE.format(dishes=get_dishes(num_choice, menu)))
    return


def get_dishes(number, menu=MENU):
    """Form a random combination of dishes"""
    sel = list(menu)

    res = []
    for i in range(number):
        rnd = random.choice(sel)
        res.append(rnd)
        res.append(random.choice(JOINTS))
    res = res[:-1]

    return ''.join(res)


def main():
    """Gets called when run as a script."""
    parser = argparse.ArgumentParser(description='Vikings restaurant menu generator.')
    parser.add_argument('num_dishes', type=int, default=DEF_CHOICE, nargs='?',
                        help='number of dishes to include in the menu')
    parser.add_argument('--menu', type=str, nargs='+',
                        help='a list of dishes to include in the menu')

    args = parser.parse_args()

    # If menu argument is passed, extend the default MENU list with the new items
    if args.menu:
        menu = MENU + args.menu
    else:
        menu = MENU

    dialog(args.num_dishes, menu)


if __name__ == '__main__':
    main()
