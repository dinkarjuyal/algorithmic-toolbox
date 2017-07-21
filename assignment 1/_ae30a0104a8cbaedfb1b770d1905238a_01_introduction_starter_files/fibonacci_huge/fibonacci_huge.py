# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    f=1
    s=1
    t=1
    if n <= 1:
        return n
    p = 0 #period, formula taken from wiki
    if m % 2 == 0: 
        if(m / 2 > 1):
            p = 8 * (m / 2) + 4
        else:
            p = 3 
    
    else:
        if ((m + 1) / 2) > 1:
            p = 4 * ((m + 1) / 2)
        else:
            p = 1;
    

    revised_n = n % p

    i=2
    
    while i < revised_n:
        t = f + s
        f = s
        s = t
        i += 1
    return t%m    
        

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
