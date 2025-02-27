def prime_factors(nums):
    if len(nums) <= 19:
        return set()
    n = nums[19]
    prime_factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            prime_factors.add(i)
            n //= i
    return prime_factors