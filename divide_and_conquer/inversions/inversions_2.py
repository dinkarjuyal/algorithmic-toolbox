# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    number_of_inversions += merge(a, b, left, ave, right)
    return number_of_inversions

def merge(a,b,left, ave, right):
    c = []
    i = left
    j = ave
    k = left
    n = 0
    while (i <= ave and j < right):
        if a[i]<=a[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(a[j])
            print (a[i],a[j])
            j+=1
            n+=(ave-i)
            
    while (i < ave):
        b.append(a[i])
        i+=1
    while (j < right):
        b.append(a[j])
        j+=1
    c.extend(b)    
       
    return n    
        
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))

