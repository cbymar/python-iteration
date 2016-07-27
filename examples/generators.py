#!/usr/bin/env python


def build_list_of_squares(n):
    """Shows an example of building a list of squares."""
    return [x ** 2 for x in range(n)]


def generate_squares(n):
    """Shows an example of generating squares using a generator."""
    for x in xrange(n):
        yield x ** 2


def generate_squares_with_expression(n):
    """The above function may be rewritten thusly."""
    return (x ** 2 for x in xrange(n))


def square_generator_exploded(n):
    """An exploded view of a generator."""
    print 'Beginning iteration.'
    for x in xrange(n):
        print 'Iterating...'
        yield x ** 2
        print 'Iteration paused.'
    print 'Iteration stopped.'


def get_sum_squares():
    """Performs simple math against a generator.

    This is meant as an example of code where previous
    data is not needed.
    """
    sum_squares = 0
    for x in square_generator_exploded(10):
        sum_squares += x
    return sum_squares

if __name__ == '__main__':
    print build_list_of_squares(10)
    print generate_squares(10)
    print list(generate_squares_with_expression(10))
    print list(square_generator_exploded(10))
    print get_sum_squares()
