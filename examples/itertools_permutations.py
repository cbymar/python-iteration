#!/usr/bin/env python

import itertools


def get_permutations(word):
    for permutation in itertools.permutations(word):
        print permutation

if __name__ == '__main__':
    get_permutations('fork')
