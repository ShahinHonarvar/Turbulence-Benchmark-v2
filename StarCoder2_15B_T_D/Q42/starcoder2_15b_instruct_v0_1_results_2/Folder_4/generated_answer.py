def prime_factors(nums):
    num = nums[15]
    prime_factors = set()
    for i in range(2, num + 1):
        if num % i == 0:
            prime_factors.add(i)
    return prime_factors