#!/usr/bin/env python

NUMBERS_TO_SQUARE = [1, 2, 3, 4, 5]


def dictionary_comprehension():
    """Shows an example of a dictionary comprehension."""
    return {number: number ** 2
            for number in NUMBERS_TO_SQUARE}


def dictionary_comprehension_with_filter():
    return {number: number ** 2
            for number in NUMBERS_TO_SQUARE
            if number > 3}

if __name__ == '__main__':
    print dictionary_comprehension()
    print dictionary_comprehension_with_filter()
