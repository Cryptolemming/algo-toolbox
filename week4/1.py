#python3
# binary search

import sys
import math

def binary_search(list, nums):
    result = []
    for num in nums:
        result.append(binary_search_helper(list, num, 0, len(list)-1))
    return result

def binary_search_helper(list, num, start, end):
    if start > end:
        return -1

    mid = math.floor((start + end) / 2)
    print(mid)
    if list[mid] == num:
        return mid
    if list[mid] > num:
        return binary_search_helper(list, num, 0, mid-1)
    if list[mid] < num:
        return binary_search_helper(list, num, mid+1, end)

if __name__ == '__main__':
    list, nums = [line[1:] for line in (list(map(int, line.split())) for line in sys.stdin.read().splitlines())]
    result = binary_search(list, nums)
    print(result)
