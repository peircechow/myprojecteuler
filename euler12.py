def nfac(tn):
    counter=0
    for i in range(1,int(tn**0.5)+1):
        if tn%i==0:
            counter+=1
    return counter*2

def main():
    total=1
    var=1
    while True:
        var+=1
        total+=var
        if nfac(total)>500:
            return total
print(main())
