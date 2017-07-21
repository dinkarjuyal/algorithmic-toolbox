#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    a.sort(reverse = True)
    b.sort(reverse = True)
    max_pr = 0
    for i in range(len(a)):
        max_pr+= (a[i]*b[i])
    return max_pr    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
