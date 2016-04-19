def lf(i): #function to find the lowest prime factor of the number
    s=i
    d=2 #initial starting
    while d<s: 
        if s%d==0: #if divisible then continue to divide until
            s=s/d
        else:       #if not divisible then divisor +1
            d+=1
    return s
            

def lcm(r):
    total=1
    for i in range (1,r+1): #r=20, so will do in range from 1 to 20
        if total%i!=0:
            total = total*lf(i) #multiply by the Lowest prime fac
    return total

print(lcm(20))
