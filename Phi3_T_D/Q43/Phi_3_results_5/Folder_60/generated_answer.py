def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    start_idx, end_idx = (46, 85)
    primes_in_range = [num for num in nums[start_idx:end_idx + 1] if is_prime(num)]
    return primes_in_range