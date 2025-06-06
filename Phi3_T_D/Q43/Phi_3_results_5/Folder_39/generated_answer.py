def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    start, end = (69, 80)
    return sorted([num for num in nums[start:end + 1] if is_prime(num)])