#python3
# last digit sum of fib large n

import sys

'''
    since sum fib at n = fib of (n+2) - 1
    and since pisano period for mod 10 = 60
    find mod 10 of fib at n = (fib((n+2)%60)-1) % 10
    to represent value at place in pisano period
'''
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
    input = sys.stdin.read()
    n = int(input)
    print(last_digit_sum_fib(n))
