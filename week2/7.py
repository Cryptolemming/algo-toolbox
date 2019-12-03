#python3

# last digit partial sum of fib

import sys

"""
    last digit sum at each of from and to
    subtract the two resulting digits
    if from_digit < to_digit (fd+10) - td else fd - td
"""
# possible last digit at from - last digit at from-1 to
# get from's contribution to the sum, as the sum from m
# to n starts at m fib value, then n last digit - the result from
# previous
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
