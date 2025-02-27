def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    result = []
    for num in nums:
        if is_prime(num):
            result.append(num)
    return result