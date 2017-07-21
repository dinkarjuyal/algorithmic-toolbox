# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    start = []
    end = []
    final = []
    for s in segments:
        start.append(s.start)
        end.append(s.end)
    start.sort()
    end.sort()
    l = len(end)
    i = 0
    flag = 0
    while (i < l-1):
        final.append(end[i])
        temp = end[i]
        i = i+1
        while( temp <= end[i] and temp >= start[i] and i < l):
            if i == l-1:
                flag = 1
                break
            i = i+1
        if i == l-1 and flag == 0:
            final.append(end[i])
    return final    
        

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
