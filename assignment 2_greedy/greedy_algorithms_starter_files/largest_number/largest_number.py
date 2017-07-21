#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    while(len(a)>0):
        maxd = 0
        for num in a:
            if Greater_Equal(int(num),maxd):
                maxd = int(num)
        res+=str(maxd)
        #print maxd
        a.remove(str(maxd))
    return res                                                

def Greater_Equal(a,b):
    list_a = [int(i) for i in str(a)]
    #print (list_a)
    list_b = [int(i) for i in str(b)]
    #print (list_b)
    list_ab = list_a + list_b
    #print (list_ab)  
    list_ba = list_b + list_a
    num_ab = int(''.join(str(i) for i in list_ab))
    num_ba = int(''.join(str(i) for i in list_ba))
    if num_ab > num_ba:
        return True
    else:
        return False
    # another method, here I compare digit by digit
    '''for i in range(min(len(list_a),len(list_b))):
        if list_a[i] > list_b[i]:
            return True
        elif list_a[i] < list_b[i]:
            return False
    #control will come out of loop if all common digits are same
    if len(list_a) > len(list_b):
        if list_a[len(list_b)] > list_b[0]:
            return True
        else:
            return False
    if len(list_b) > len(list_a):
        if list_b[len(list_a)] > list_a[0]:
            return False
        else:
            return True   ''' 
   
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
