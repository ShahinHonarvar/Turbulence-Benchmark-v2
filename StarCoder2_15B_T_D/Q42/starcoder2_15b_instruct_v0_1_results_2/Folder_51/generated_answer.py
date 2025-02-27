def prime_factors(nums):
    num = nums[64]
    prime_factors = set()
    for i in range(2, num + 1):
        while num % i == 0:
            prime_factors.add(i)
            num //= i
    return prime_factors