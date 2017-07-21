# Uses python3
import sys

def fibonacci_partial_sum_naive(m, n):
    #sum upto n numbers
    f=1
    s=1
    t=1
    sum1 = 2
    if n == 0:
        return sum1-2
    i=2   
    while i < n:
        t = (f + s)%10
        f = s%10
        s = t
        i += 1
        sum1 = sum1+t

#sum upto m-1 numbers
    k= m - 1
    f=1
    s=1
    t=1
    sum2 = 2
    if k == 0:
        sum2= sum2-2
    i=2   
    while i < k:
        t = (f + s)%10
        f = s%10
        s = t
        i += 1
        sum2 = (sum2+t)%10

    return int((sum1 - sum2)%10)    
  

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
