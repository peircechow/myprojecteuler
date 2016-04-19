def is_py(a,b):
    
    c_sqed=a*a+b*b
    if (c_sqed**0.5)%1==0 and a+b+c_sqed**0.5==1000:#check if integer/whole number
        
        return True
    return False

def main():
    i=500
    j=500
    for a in range(i,1,-1):
        for b in range(j,1,-1):
            c=1000-a-b
            if is_py(a,b)==True and a+b+c==1000:
                
                print(a)    
                print(b)
                print(c)
                return a*b*c
print(main())

   
