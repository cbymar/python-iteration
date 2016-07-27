#!/usr/bin/env python

NUMBERS_TO_SQUARE = [1, 2, 3, 4, 5]


def generator_expression():
    """Shows an example of a generator expression."""
    return (number ** 2 for number in NUMBERS_TO_SQUARE)

if __name__ == '__main__':
    # The generator expression creates a generator object.
    print generator_expression()
    for x in generator_expression():
        print x
