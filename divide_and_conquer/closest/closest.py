#Uses python3
import sys
import math
import random



def partition3(a, l, r):
    #write your code here
    x = a[l]
    j = l
    k = l
    for i in range(l + 1, r + 1):
        if a[i] < x and j!=k:
            j += 1
            k += 1
            a[i], a[j] = a[j], a[i]
            a[i], a[k] = a[k], a[i]
        elif a[i] < x and j==k:
            j += 1
            k += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
    a[l], a[j] = a[j], a[l]    
    return j,k

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
    print (a,l,r)
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    #m = partition2(a, l, r)
    m1,m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);



    
def minimum_distance(x, y):
    #write your code here
    print (x,y)
    randomized_quick_sort(x, 0, len(x) - 1)
    randomized_quick_sort(y, 0, len(y) - 1)
    print (x,y)
    
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
    
