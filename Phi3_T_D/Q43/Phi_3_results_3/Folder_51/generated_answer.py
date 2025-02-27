def find_primes_between_indices(nums):
    return sorted([num for num in nums[13:69] if all((num % div != 0 for div in range(2, int(num ** 0.5) + 1)))], reverse=True)