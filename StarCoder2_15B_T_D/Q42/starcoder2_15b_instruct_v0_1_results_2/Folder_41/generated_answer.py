def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(nums):
    if len(nums) < 84:
        return set()
    num = nums[84]
    return set((i for i in range(2, num + 1) if is_prime(i) and num % i == 0))