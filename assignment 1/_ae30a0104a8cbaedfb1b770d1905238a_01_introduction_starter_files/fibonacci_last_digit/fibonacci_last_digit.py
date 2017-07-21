# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):  

    f=1
    s=1
    t=1

    if n <= 1:
        return n
    i=2
    
    while i < n:
        t = (f + s)%10
        f = s%10
        s = t
        i += 1
    return t    

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
