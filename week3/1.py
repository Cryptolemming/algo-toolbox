# money change

import sys

def get_money_change(n):
    count = 0
    if n <= 0: return 0
    denominations = [10,5,1]

    for i in denominations:
        count = count + int(n / i)
        n = n % i

    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_money_change(n))
