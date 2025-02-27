def find_primes_between_indices(nums):
    is_prime = [True] * len(nums)
    for i in range(2, int(len(nums) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, len(nums), i):
                is_prime[j] = False
    primes = [num for num, is_prime in zip(nums, is_prime) if is_prime]
    return sorted(primes[24:33], reverse=True)