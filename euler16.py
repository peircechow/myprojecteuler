def main():
    P=1000
    I=2
    total=0
    for j in str(I**P):
        total+=int(j)
    return total

print(main())
