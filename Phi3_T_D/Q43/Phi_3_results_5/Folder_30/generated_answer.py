def find_primes_between_indices(nums, start_index=61, end_index=80):
    primes = []
    for i in range(start_index, end_index + 1):
        if all((i % n != 0 for n in range(2, int(i ** 0.5) + 1))):
            primes.append(nums[i])
    return sorted(primes, reverse=True)