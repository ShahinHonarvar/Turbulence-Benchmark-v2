from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    if len(nums) > 56 or not isinstance(nums[56], int) or nums[56] <= 0:
        return set()
    factors = set()
    candidate = 2
    while candidate * candidate <= nums[56]:
        if nums[56] % candidate == 0:
            nums[56] //= candidate
            if is_prime(candidate):
                factors.add(candidate)
        else:
            candidate += 1
    if nums[56] > 1 and is_prime(nums[56]):
        factors.add(nums[56])
    return factors