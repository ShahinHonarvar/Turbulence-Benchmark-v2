def find_primes_between_indices(nums):
    n = len(nums)
    is_prime = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    primes = [num for i, num in enumerate(nums) if i >= 229 and i <= 850 and is_prime[i]]
    return sorted(primes, reverse=True)