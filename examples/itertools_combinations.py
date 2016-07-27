#!/usr/bin/env python

import itertools


def get_combinations(word):
    for combination in itertools.combinations(word, len(word) / 2):
        print combination

if __name__ == '__main__':
    get_combinations('fork')
