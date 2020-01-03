#python3
# maximum number of prizes

import sys

def max_prizes(n):
    result = []
    i = 1
    while n > 0:
        diff = n - i
        if diff > i:
            result.append(str(i))
            n -= i
            i += 1
        else:
            result.append(str(n))
            n -= n

    return result;


if __name__ == '__main__':
    input = int(sys.stdin.read())
    result = max_prizes(input)
    print(len(result))
    print(" ".join(result))
