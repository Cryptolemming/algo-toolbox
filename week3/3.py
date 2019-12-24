# car fueling
import sys

def min_number_stops(d, m, stops):
    stops.append(d)
    min_stops = 0
    previous = 0
    remaining = m - stops[0]

    for idx, dist in enumerate(stops[:-1]):
        dist_to_next = stops[idx+1] - dist

        if dist_to_next > m:
            return -1

        if dist_to_next > remaining:
            min_stops+=1
            remaining = m

        remaining-=dist_to_next
        previous = dist

    return min_stops

if __name__ == "__main__":
    input = list(map(int, sys.stdin.read().split()))
    print(input)
    d, m = input[:2]
    stops = input[3:]
    print(min_number_stops(d, m, stops))
