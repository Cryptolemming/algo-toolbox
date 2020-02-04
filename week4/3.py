# Uses python3
import sys
import random
import math

def partition3(a, l, r):
    #write your code here
    x = a[l]
    j = l
    i = l+1

    for p in range(l+1, r+1):
        if a[p] == x:
            a[p], a[i] = a[i], a[p]
            i+=1

        if a[p] < x:
            if p > i:
                i+=1
                a[p], a[i] = a[i], a[p]
            a[i], a[j] = a[j], a[i]
            i+=1
            j+=1

    print(a)

    return math.floor((j+i)/2)

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
