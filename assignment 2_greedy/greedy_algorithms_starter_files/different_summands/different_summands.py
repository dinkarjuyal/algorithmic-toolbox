# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    l = 1
    if n<=2:
        summands.append(n)
        return summands
    temp = n # for case of n = 3    
    while(n > (2*l)):
        summands.append(l)
        n = n-l
        l = l+1
        if n<=2:
            summands.append(n)
    if temp!= 3:        
        summands.append(n)        
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print (len(summands))
    for x in summands:
        print (x, end=' ')
