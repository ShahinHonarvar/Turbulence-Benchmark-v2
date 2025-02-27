def find_primes_between_indices(nums):
    primes = []
    for i in range(61, 81):
        is_prime = True
        for j in range(2, nums[i] // 2 + 1):
            if nums[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(nums[i])
    primes.sort(reverse=True)
    return primes