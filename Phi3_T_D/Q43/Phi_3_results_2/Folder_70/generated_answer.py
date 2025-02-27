def find_primes_between_indices(nums):
    primes = [n for n in nums[130:815] if all((n % d for d in range(2, int(n ** 0.5) + 1)))]
    return sorted(primes, reverse=True)