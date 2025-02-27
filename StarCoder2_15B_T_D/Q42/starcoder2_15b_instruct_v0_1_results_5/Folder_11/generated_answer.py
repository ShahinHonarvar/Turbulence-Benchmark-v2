def prime_factors(nums):
    limit = max(nums)
    is_prime = [True] * (limit + 1)
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    return set((p for p in primes if nums[77] % p == 0))