from sympy import *



if __name__ == '__main__':
    foo = 0
    for i in range(2*(10**6),0,-1):
        if isprime(i) == True:
            foo += i
    
    print(foo)
