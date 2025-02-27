def find_primes_between_indices(nums):
    return sorted([num for num in nums[25:63] if is_prime(num)])

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True