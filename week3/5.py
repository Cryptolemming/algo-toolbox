# collecting signatures

import sys

def min_trips(entries, segments):
    trips = 1
    segments = sorted(segments, key=lambda t: t[0])
    set = [str(segments[0][1])]
    target = max = segments[0][1]

    for i in range(1, entries):
        coord = segments[i]
        if coord[0] <= target:
            if coord[1] > max: max = coord[1]
        else:
            trips += 1
            if coord[0] <= max:
                target = max
                max = coord[1]
            else:
                target = max = coord[1]
            set.append(str(target))

    return { 'trips': trips, 'set': set }

if __name__ == '__main__':
    entries = int(sys.stdin.readline())
    segments = [(line[0], line[1]) for line in (list(map(int, line.split())) for line in sys.stdin.read().splitlines())]
    result = min_trips(entries, segments)
    print(result['trips'])
    print(" ".join(result['set']))
