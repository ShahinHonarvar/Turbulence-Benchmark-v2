def find_primes_between_indices(nums):
    primes = [num for i, num in enumerate(nums) if i >= 16 and i <= 25 and all((num % n != 0 for n in range(2, int(num ** 0.5) + 1)))]
    return sorted(primes, reverse=True)