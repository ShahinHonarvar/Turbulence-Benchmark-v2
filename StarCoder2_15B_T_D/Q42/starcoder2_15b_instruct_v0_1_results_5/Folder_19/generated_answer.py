def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(nums):
    prime_factors = set()
    num = nums[13]
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            prime_factors.add(i)
    return prime_factors