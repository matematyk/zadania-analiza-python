def primeFactor(n):
    factors = []
    while n % 2 == 0:
        n = n//2
        factors.append(2)

    for i in range(3, int(n ** (1/2)),2):
        while n % i == 0: 
            n = n//i
            factors.append(i)

    ## prime case
    if n > 2: 
        factors.append(n)
    return factors

print(primeFactor(12345))