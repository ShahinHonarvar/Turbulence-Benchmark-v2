def find_primes_between_indices(nums):
    start, end = (23, 48)
    primes = [num for i, num in enumerate(nums) if start <= i <= end and all((num % div != 0 for div in range(2, int(num ** 0.5) + 1)))]
    return sorted(primes)