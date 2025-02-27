def prime_factors(integers):
    limit = max(integers)
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    prime_factors = []
    for i in range(len(integers)):
        n = integers[i]
        if is_prime[n]:
            prime_factors.append(n)
        else:
            for j in range(2, n + 1):
                if is_prime[j] and n % j == 0:
                    prime_factors.append(j)
                    while n % j == 0:
                        n //= j
    return set(prime_factors) if len(integers) >= 64 else None