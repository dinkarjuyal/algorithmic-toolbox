# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    major_1 = get_majority_element(a, left,(left + right - 1)//2 + 1)
    major_2 = get_majority_element(a,(left + right - 1)//2 + 1, right)
    #print ("major %d %d"%(major_1, major_2))
    c1 = c2 =0
    for i in range(left,right):
        if a[i] == major_1:
            c1+=1
            #print (c1)
        if a[i] == major_2:
            c2+=1
            #print (c2)
    if c1 > (right - left)//2:
        return major_1
    if c2 > (right - left)//2:
        return major_2
    
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
