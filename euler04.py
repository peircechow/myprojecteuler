def is_p(n):
    return str(n)==str(n)[::-1]

def cb():
    s=999*999
    for n in range(s,1,-1):
        if is_p(n): #if number is palindrome
            for j in range (999,99,-1): #finding the 3 digits factor
                if n%j==0: #check if factor
                    if len(str(int(n/j)))==3: #check if factor has 3 digits
                        return n

print(cb())
