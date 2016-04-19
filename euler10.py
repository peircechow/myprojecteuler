def is_prime(i):
    if i==1:
        return False
    for a in range (2,int(i**0.5)+1):
        if i%a==0 or i==1:
            return False
    return True

def main(x):
    total=0
    for i in range(1,x):
        if is_prime(i):
            total+=i
    return total

x=2000000

print(main(x))
