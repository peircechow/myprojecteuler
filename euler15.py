def fac(n):
    total=1
    for i in range(1,n+1):
        total=total*i
    return total

def main():
    X=20
    Y=20
    #total 40 moves, 20 which are right 20 which are down
    #hence we use 40 choose 20
    comb= (fac(X+Y)/fac(X))/fac(Y) #refer to combinations and permutations (honestly idk how they derive this ._.)
    return comb
print(main())

