#!/usr/bin/env python

import itertools

LIST_1 = ['A', 'B', 'C', 'D', 'E']
LIST_2 = [1, 2, 3, 4, 5]


def concatenate_lists():
    """Don't do this."""
    return LIST_1 + LIST_2


def chain_lists_together():
    chain = itertools.chain(LIST_1, LIST_2)
    print chain
    print list(chain)


def ifilter_iterable():
    iterable = [5, 10, 15, 20, 25, 30]

if __name__ == '__main__':
    print concatenate_lists()
    chain_lists_together()
