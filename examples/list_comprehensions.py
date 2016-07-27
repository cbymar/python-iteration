#!/usr/bin/env python

NUMBERS_TO_SQUARE = [1, 2, 3, 4, 5]


def append_to_list():
    """Shows a roundabout way to build a list. Don't do this."""
    squared_numbers = []
    for number in NUMBERS_TO_SQUARE:
        squared_number = number ** 2
        squared_numbers.append(squared_number)
    return squared_numbers


def list_comprehension():
    """Shows an example of a list comprehension. This is preferred."""
    return [number ** 2
            for number in NUMBERS_TO_SQUARE]


def list_comprehension_with_filter():
    """Shows an example of a list comprehension with a filter."""
    return [number ** 2
            for number in NUMBERS_TO_SQUARE
            if number > 3]

if __name__ == '__main__':
    print append_to_list()
    print list_comprehension()
    print list_comprehension_with_filter()
