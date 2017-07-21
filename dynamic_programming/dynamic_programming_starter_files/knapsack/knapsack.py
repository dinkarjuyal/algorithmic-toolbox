# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    '''result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result'''
    items = len(w)
    #print (items)
    table = [[0]*(W+1) for i in range(items+1)]
    #print (table)
    for i in range(1,items+1):
        for j in range(1,W+1):
            #print (i,j)
            table[i][j] = table[i-1][j]
            if w[i-1] <= j :
                temp = table[i-1][j-w[i-1]]+w[i-1]# to see value before adding the ith item
                if table[i][j] < temp:
                    table[i][j] = temp
                    #print (table[i][j])
                    
    return table[items][W]                    
                    

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W,w))
   
