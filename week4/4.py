#uses python3
import sys
import math

def number_of_inversions(n, list):
    # mergesort returning # of inversions
    return merge_sort(list, 0, n - 1)

def merge_sort(list, l, r):
    if l >= r:
        return 0
    m = int((l+r)/2)
    inversionsL = merge_sort(list, l, m)
    inversionsR = merge_sort(list, m + 1, r)
    return merge(list, l, m, r) + inversionsL + inversionsR

def merge(list, l, m, r):
    r_pointer = m + 1
    inversions = 0

    while l <= m & r_pointer <= r:
        if list[l] > list[r_pointer]:
            temp = list[r_pointer]
            list[r_pointer] = list[l]
            list[l] = temp
            l += 1
            inversions += 1
        else:
            l += 1

    if l <= m:
        list[]

    print(list)
    return inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    result = number_of_inversions(n, a)
    print(result)
