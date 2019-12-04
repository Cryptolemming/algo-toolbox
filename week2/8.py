#python3
# last digit of sum of squares of fib

from sys import stdin

# last digit sum of squares at n = ((last digit at n) * (last digit at n + 1)) % 10
def last_digit_sum_squares_fib(n):
    if n <= 2: return n

    last_digits = last_digits_fib(n+1)

    return (last_digits[0] * last_digits[1]) % 10

def last_digits_fib(n):
    n = (n) % pisano_period(10)
    n_one, n_two = 0, 1
    for i in range(2, n+1):
        n_one, n_two = n_two, (n_one + n_two) % 10

    return [n_one, n_two]

def pisano_period(m):
    previous, current = 0, 1
    end = m * m

    for i in range(end):
        mod = (previous + current) % m
        previous, current = current, mod
        if previous == 0 and current == 1:
            return i + 1

if __name__ == '__main__':
    n = int(stdin.read())
    print(last_digit_sum_squares_fib(n))
