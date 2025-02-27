def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    if len(nums) < 702:
        raise ValueError('Index out of range')
    n = nums[702]
    prime_factors = set()
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            prime_factors.add(i)
    return prime_factors