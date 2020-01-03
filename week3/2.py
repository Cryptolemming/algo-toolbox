#python3
# maximum value of the loot

import sys

def max_value_of_loot(capacity, values, weights):
    max_value = 0
    ratios = sorted(enumerate([v / w for v, w in zip(values, weights)]), key=lambda r: r[1], reverse=True)
    i = 0
    ratios_length = len(ratios)
    while capacity > 0 and i < ratios_length:
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
    print("{:.3f}".format(max_value_of_loot(capacity, values, weights)))
