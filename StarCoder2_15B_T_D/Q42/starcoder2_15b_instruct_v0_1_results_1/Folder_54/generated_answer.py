def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(nums):
    if len(nums) < 52:
        return []
    num = nums[51]
    prime_factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            if is_prime(i):
                prime_factors.append(i)
            num //= i
    return set(prime_factors)