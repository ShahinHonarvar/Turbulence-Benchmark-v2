def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    if len(nums) < 986:
        return set()
    n = nums[985]
    prime_factors = set()
    if is_prime(n):
        prime_factors.add(n)
    else:
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                prime_factors.add(i)
    return prime_factors