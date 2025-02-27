def find_primes_between_indices(nums):
    start, end = (40, 68)
    primes = [num for num in nums[start:end + 1] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and num > 1]
    return sorted(primes, reverse=True)