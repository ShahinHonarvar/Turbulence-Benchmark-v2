def find_primes_between_indices(nums):
    is_prime = [True] * len(nums)
    for i in range(2, int(len(nums) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, len(nums), i):
                is_prime[j] = False
    primes = [num for i, num in enumerate(nums) if is_prime[i] and 15 <= i <= 48]
    primes.sort(reverse=True)
    return primes