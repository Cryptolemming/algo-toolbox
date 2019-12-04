#python3

# last digit partial sum of fib

import sys

"""
    since we start at the contribution to sum of from_,
    get modulo 10 subtraction of to - (from_ - 1)
"""
def last_digit_partial_sum_fib(from_, to):
    if from_ <= 1: return last_digit_sum_fib(to)

    return subtract_modulo_10(last_digit_sum_fib(from_-1),
                              last_digit_sum_fib(to))

def subtract_modulo_10(from_, to):
    return to + 10 - from_ if to < from_ else to - from_

def last_digit_sum_fib(n):

    n = (n+2) % pisano_period(10)
    n_one, n_two = 0, 1
    for i in range(2, n+1):
        mod = (n_one + n_two) % 10
        n_one, n_two = n_two, mod

    return 9 if n_two == 0 else n_two - 1

def pisano_period(m):
    previous, current = 0, 1
    end = m * m

    for i in range(end):
        mod = (previous + current) % m
        previous, current = current, mod
        if previous == 0 and current == 1:
            return i + 1

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(last_digit_partial_sum_fib(from_, to))
