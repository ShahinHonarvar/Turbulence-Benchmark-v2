def find_primes_between_indices(nums):
    n = len(nums)
    is_prime = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    primes = []
    for i in range(61, 80):
        if is_prime[i] and nums[i] > 1:
            primes.append(nums[i])
    primes.sort()
    return primes