def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    result = [nums[i] for i in range(37, 96) if is_prime(nums[i])]
    result.sort(reverse=True)
    return result