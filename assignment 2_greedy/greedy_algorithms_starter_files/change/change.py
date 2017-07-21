# Uses python3
import sys

def get_change(m):
    #write your code here
    values = [10, 5, 1]
    l = len(values)
    c = 0
    if m <= 0:
        return 0
    while(m > 0):
        for i in range (l):
            if m >= values[i]:
                c += (m // values[i])
                m = m % values[i]
    return c

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
