# Uses python3
import math
def evalt(a, opr, b):
    if opr == '+':
        #print (a+b)
        return a + b
    elif opr == '-':
        return a - b
    elif opr == '*':
        return a * b
    else:
        assert False

def min_and_max(i,j,M,m,op):
    min1 = math.inf
    max1 = -math.inf
    #print(i,j)
    for k in range(i,j):
        #print(k,j)
        a = evalt(M[i-1][k-1],op[k-1],M[k][j-1])
        b = evalt(M[i-1][k-1],op[k-1],m[k][j-1])
        c = evalt(m[i-1][k-1],op[k-1],M[k][j-1])
        d = evalt(m[i-1][k-1],op[k-1],m[k][j-1])
        min1 = min(min1,a,b,c,d)
        max1 = max(max1,a,b,c,d)
    return(min1,max1)


def get_maximum_value(dataset):
    #write your code here
    num = []
    op = []
    for i in range(len(dataset)):
        if i%2 == 0:
            num.append(int(dataset[i]))
        else:
            op.append(dataset[i])
    #print(num,op)
    l = len(num)
    M = [[0]*l for i in range(l)]
    m = [[0]*l for i in range(l)]
    for i in range(0,l):
        m[i][i] = M[i][i] = num[i]
    #print(m,M,l)    
    for s in range(1,l):
        for i in range(1,l+1-s):
            j = i+s
            m[i-1][j-1],M[i-1][j-1] = min_and_max(i,j,M,m,op)
    #print(M)        
    return M[0][l-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
