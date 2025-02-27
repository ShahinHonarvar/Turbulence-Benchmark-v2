def find_primes_between_indices(nums):
    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    primes = []
    for i in range(60, 96):
        if is_prime[nums[i]]:
            primes.append(nums[i])
    primes.sort()
    return primes