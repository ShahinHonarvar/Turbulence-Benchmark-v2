def find_primes_between_indices(nums):
    result = []
    for i in range(46, 86):
        if is_prime(nums[i]):
            result.append(nums[i])
    return sorted(result)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True