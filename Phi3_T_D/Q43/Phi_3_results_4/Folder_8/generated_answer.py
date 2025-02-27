def find_primes_between_indices(nums):
    primes = [num for num in nums[43:77] if all((num % div != 0 for div in range(2, int(num ** 0.5) + 1))) and num > 1]
    return sorted(primes, reverse=True)