# Uses python3
def edit_distance(s, t):
    #write your code here
    s = list(s)
    t = list(t)
    len_1 =len(s)
    len_2 =len(t)
    dist = [[0]*(len_2 + 1) for i in range(len_1 + 1)]
    #print (len_1,len_2)
    for i in range(len_2+1):
        dist[0][i] = i
    for i in range(len_1+1):
        dist[i][0] = i
    #print (dist)    
    for i in range(1,len_1+1):
        for j in range(1,len_2+1):
            ins = dist[i][j-1]+1
            delete = dist[i-1][j]+1
            match = dist[i-1][j-1]
            mismatch = dist[i-1][j-1]+1
            #print (i,j)
            if s[i-1] == t[j-1]:
                dist[i][j] = min(ins,delete,match)
            else:
                dist[i][j] = min(ins,delete,mismatch)
    #print (dist)
    return dist[len_1][len_2]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
