def even(n):
    return n/2
def odd(n):
    return 3*n+1

def main():
    N=1000000
    big_num=0
    big_count=0
    for i in range(1,N):
        counter=1 #counts number of times the particular number can generate how many terms in the sequence
        j=i 
        while i!=1:
            if i%2==0:
                i=even(i)
            else:
                i=odd(i)
            counter+=1
        if counter>big_count:
            big_count=counter
            big_num=j
    return big_num

print(main())
