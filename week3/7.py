#python3
# maximum salary

import sys

def max_salary(n, nums):
    result = ''
    first_digit_map = {}

    # map by value of first digit then by length of number
    for num in nums:
        first_digit = int(num[0])
        length = len(num)
        if first_digit in first_digit_map:
            by_length = first_digit_map[first_digit]
            if length in by_length:
                by_length[length].append(num)
            else:
                by_length[length] = [num]
        else: first_digit_map[first_digit] = {length: [num]}

    # iterate by sorted first digit then by sorted length then concatenat sorted list
    sorted_first_digit_items = dict(sorted(first_digit_map.items(), reverse=True)).items()
    for k, items in sorted_first_digit_items:
        by_length_sorted = dict(sorted(items.items()))
        for by_length_k, by_length_items in by_length_sorted.items():
            result += "".join([item for item in sorted(by_length_items, key=lambda by_length_item: len(by_length_item))])

    return result

if __name__ == '__main__':
    n = map(int, sys.stdin.readline())
    nums = list(sys.stdin.read().split())
    print(max_salary(n, nums))
