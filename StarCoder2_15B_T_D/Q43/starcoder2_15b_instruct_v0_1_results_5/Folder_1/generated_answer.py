def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    result = []
    for i in range(len(nums)):
        if is_prime(nums[i]) and 87 <= i <= 89:
            result.append(nums[i])
    result.sort()
    return result