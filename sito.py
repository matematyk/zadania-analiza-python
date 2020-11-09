def sito(n):
    sieve = {}
    for x in range(2,n+1):
        sieve[x] = x

    for i in range(2, int(n ** 1/2)):
        if sieve[i]:
            j = 2
            u = 1
            while u < n:
                u = i * j
                j = j+ 1
                sieve[u] = None
    return sieve

print(sito(10))  