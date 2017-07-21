# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    for i in range(len(starts)):
        starts[i] = (starts[i],'l')
        ends[i] = (ends[i],'r')
    for i in range(len(points)):
        points[i] = (points[i],'p')
    #print(starts,ends, points)
    combined = starts + ends + points
    #print (combined)
    combined = sorted(combined, key =lambda x: (x[0],x[1]))
    #print (combined)
    n = 0
    c ={}
    for i in range(len(combined)):
        if combined[i][1]=='l':
            n += 1
        if combined[i][1]=='r':
            n -= 1
        if combined[i][1]=='p':
            c[combined[i][0]]=n
    #print (c)
    for i in range(len(points)):
        cnt[i] = c[points[i][0]]
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
