def find_primes_between_indices(nums):
    is_prime = [True] * len(nums)
    for i in range(2, int(len(nums) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, len(nums), i):
                is_prime[j] = False
    primes = []
    for i in range(56, 58):
        if is_prime[i] and i >= 0:
            primes.append(nums[i])
    primes.sort(reverse=True)
    return primes