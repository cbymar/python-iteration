#!/usr/bin/env python

import itertools


def repeat_list(list_to_repeat, times_to_repeat):
    """Shows an example of a repeated list with a limit."""
    for repeated_list in itertools.repeat(list_to_repeat, times_to_repeat):
        yield repeated_list


if __name__ == '__main__':
    list_to_repeat = ['a', 'b', 'c']
    times_to_repeat = 10
    print list(repeat_list(list_to_repeat, times_to_repeat))
