#!/usr/bin/env python3
import random
import string
import argparse


def password_generator(length, complexity):
    """Generate a random password of given length and complexity."""

    # Define different sets of characters for different complexity levels
    all_characters = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation
    ]

    # Start with a set of lower case characters
    password_characters = all_characters[0]

    # Based on the given complexity, add more character sets
    for i in range(1, complexity):
        password_characters += all_characters[i % len(all_characters)]

    # Generate the random password
    password = ''.join(random.choice(password_characters) for i in range(length))

    print(f'Your generated password is: {password}')


def main():
    """Gets called when run as a script."""
    parser = argparse.ArgumentParser(description='Random password generator.')
    parser.add_argument('length', type=int, help='Desired password length')
    parser.add_argument('complexity', type=int, choices=range(1, 5),
                        help='Password complexity level (1 to 4)')

    args = parser.parse_args()

    password_generator(args.length, args.complexity)


if __name__ == '__main__':
    main()
