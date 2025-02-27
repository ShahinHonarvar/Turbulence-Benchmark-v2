def find_primes_between_indices(nums):
    primes = []
    for val in nums[31:68]:
        if val > 1:
            for i in range(2, int(val ** 0.5) + 1):
                if val % i == 0:
                    break
            else:
                primes.append(val)
    return sorted(primes, reverse=True)