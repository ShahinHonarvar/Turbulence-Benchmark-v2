def find_primes_between_indices(nums):
    limit = max(nums)
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    primes = []
    for i in range(len(nums)):
        if is_prime[nums[i]]:
            primes.append(nums[i])
    primes.sort()
    return primes