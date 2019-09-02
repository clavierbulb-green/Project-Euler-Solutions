'''
Solution to Project Euler Problem 3:
'''
def largestPrimeFactor(x):
    '''
    Returns largest prime factor of a given integer {x}
    '''
    factors = []
    # find factors
    for i in range(2, x//2 + 1):
        print(i)
        if x % i == 0:
            factors.append(i)

    # if x has no factors, x is prime, so it is its own largest prime factor
    if not factors:
        return x

    # filter out non-prime factors
    prime_factors = set(factors)
    for i in range(0, len(factors)):
        for j in range(2, 10):
            if factors[i] % j == 0 and factors[i] not in [2, 3, 5, 7]:
                prime_factors.discard(factors[i])

    return max(prime_factors)


target = 600851
factor = largestPrimeFactor(target)
print(f"Largest prime factor of {target}: {factor}")
