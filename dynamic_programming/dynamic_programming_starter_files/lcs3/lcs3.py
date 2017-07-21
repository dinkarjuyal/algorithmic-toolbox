#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    l = len(a)
    m = len(b)
    n = len(c)
    lis = [l,m,n]
    lis = sorted(lis)
    dim_1 = lis[0]
    dim_2 = lis[1]
    dim_3 = lis[2]
    arr_1 = []
    arr_2 = []
    arr_3 = []
    if l == dim_1:
        arr_1.extend(a)
        if m == dim_2:
            arr_2.extend(b)
            arr_3.extend(c)
        else:
            arr_2.extend(c)
            arr_3.extend(b)
    elif m == dim_1:
        arr_1.extend(b)
        if l == dim_2:
            arr_2.extend(a)
            arr_3.extend(c)
        else:
            arr_2.extend(c)
            arr_3.extend(a)
    elif n == dim_1:
        arr_1.extend(c)
        if l == dim_2:
            arr_2.extend(a)
            arr_3.extend(b)
        else:
            arr_2.extend(b)
            arr_3.extend(a)        
        
    #print(dim_1,dim_2,dim_3)
    #print(arr_1,arr_2,arr_3)
    table = [[[0 for i in range(dim_1+1)] for j in range(dim_2+1)] for k in range(dim_3+1)]
    #print (table)
    #print (l,m,n)
    #print (len(table))
    #print (len(table[0]))
    #print (len(table[0][0])) 
    for i in range(dim_3+1):
        for j in range(dim_2+1):
            for k in range(dim_1+1):
                #print (i,j,k)
                if i==0 or j==0 or k==0: #any string is empty
                    table[i][j][k] = 0
                elif(arr_3[i-1] == arr_2[j-1] and arr_3[i-1] == arr_1[k-1]):
                    table[i][j][k] = table[i-1][j-1][k-1] + 1
                else:
                    table[i][j][k] = max(table[i-1][j][k], table[i][j-1][k], table[i][j][k-1])# table[i-1][j-1][k], table[i-1][j][k-1], table[i][j-1][k-1])

    #print (table)                 
    return table[dim_3][dim_2][dim_1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
