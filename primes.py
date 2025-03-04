def primes(a,b):
    for n in range (a,b):
        for x in range (2,n):
            if n %x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            print(n, 'is a prime number')