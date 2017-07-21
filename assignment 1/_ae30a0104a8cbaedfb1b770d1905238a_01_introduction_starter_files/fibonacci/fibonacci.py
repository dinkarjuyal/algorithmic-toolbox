# Uses python3
def calc_fib(n):
    f=1
    s=1
    t=1
    assert(n >= 0 and n <= 45)
    if n <= 1:
        return n
    i=2
    
    while i < n:
        t = f + s
        f = s
        s = t
        i += 1
    return t    
        
    

n = int(input())
print(calc_fib(n))
