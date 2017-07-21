# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    '''while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)'''
    op = [0]*(n+1) # contains no of operations to reach nth number
    op[0] = -1
    for i in range(1, n+1):
        op[i] = op[i - 1] + 1
        if i%2 == 0:
            #print (i)
            op[i] = min(1 + op[int(i/2)],op[i])
        if i%3 == 0:
            op[i] = min(1 + op[int(i/3)],op[i])
            
    #print (op)        
    while (i > 1):
        sequence.append(i)
        #print (i)
        if i%3 == 0 and op[int(i/3)] == op[i] - 1:
            i =int(i/3)
        elif i%2 == 0 and op[int(i/2)] == op[i] - 1:
            i =int(i/2)
            #print ('f %d'%(i))
        elif op[i-1] == op[i] - 1:
            i-=1    
    sequence.append(1)
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
