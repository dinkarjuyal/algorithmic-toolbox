# Uses python3
import sys

def get_inversions(a):
    if len(a) <= 1:
        return 0
    left_arr = a[:len(a)//2]
    right_arr =a[len(a)//2:]
    
    return get_inversions(left_arr) + get_inversions(right_arr) + merge(left_arr,right_arr, a)

def merge(left_a, right_a, a):
    #print (left_a, right_a)
    
    c = []
    i = j = n = k = 0
    while i < len(left_a) and j < len(right_a):
        if left_a[i] <= right_a[j]:
            a[k] = left_a[i]
            i+=1
            k+=1
        else:
            a[k] = right_a[j]
            j+=1
            k+=1
            n += (len(left_a)-i)
    while i < len(left_a):
        a[k] = left_a[i]
        i+=1
        k+=1
    while j < len(right_a):
        a[k] = right_a[j]
        j+=1
        k+=1
    #print (n)    
    return n    


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_inversions(a))



