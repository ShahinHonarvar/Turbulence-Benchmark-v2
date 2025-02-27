def find_primes_between_indices(nums):
    primes = []
    for i in range(295, 456):
        if all((nums[i] % n != 0 for n in range(2, nums[i]))):
            primes.append(nums[i])
    return sorted(primes, reverse=True)