# maximum value of the loot

import sys

def max_value_of_loot(capacity, values, weights):
    max_value = 0
    ratios = sorted(enumerate([v / w for v, w in zip(values, weights)]), key=lambda r: r[1], reverse=True)

    i = 0
    while capacity > 0:
        weight = weights[ratios[i][0]]
        value = values[ratios[i][0]]
        if capacity >= weight:
            max_value += value
        else:
            max_value += ((capacity / weight) * value)
        capacity -= weight
        i+=1

    return max_value


if __name__ == '__main__':
    input = sys.stdin.read().split()
    input = [int(i) for i in input]
    n, capacity = input[:2]
    values = input[2::2]
    weights = input[3::2]
    print("{:.4f}".format(max_value_of_loot(capacity, values, weights)))
