def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def fprime(a):
    n=1
    counter=0
    while counter<a:
        n+=1
        if is_prime(n):
            counter+=1
            
    return n

print(fprime(10001))
#i think this method is very slow lol
