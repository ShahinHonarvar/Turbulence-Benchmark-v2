def prime_factors(numbers):
    limit = max(numbers)
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    prime_factors = set()
    for prime in filter(None, is_prime):
        if numbers[478] % prime == 0:
            prime_factors.add(prime)
    return prime_factors