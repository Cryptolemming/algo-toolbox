#python3
# majority element

import sys
import math

def majority_element(count, nums):
    half = math.floor(count/2)
    element_count = {}

    for num in nums:
        if num in element_count:
            element_count[num] += 1
            if element_count[num] > half: return 1
        else: element_count[num] = 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read().splitlines()
    count, nums = int(input[0]), list(map(int, input[1].split()))
    result = majority_element(count, nums)
    print(result)
