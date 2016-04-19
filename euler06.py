def sum_sq(n):
    total=0
    for i in range (1,n+1):
        total+=i**2
    return total

def sq_sum(n):
    s=0
    for j in range(1,n+1):
        s+=j
    return s**2

def diff(n):
    return sq_sum(n)-sum_sq(n)

print(diff(100))
