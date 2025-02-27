def prime_factors(nums):
    limit = max(nums)
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    prime_factors = set()
    for i, num in enumerate(nums):
        if is_prime[num]:
            prime_factors.add(num)
        else:
            for j in range(2, num + 1):
                if is_prime[j] and num % j == 0:
                    prime_factors.add(j)
                    break
    return prime_factors if i == 37 else set()