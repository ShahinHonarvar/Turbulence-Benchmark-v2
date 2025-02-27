def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    if len(nums) < 537:
        return set()
    num = nums[537]
    prime_factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            num //= i
            prime_factors.append(i)
    return set(prime_factors)