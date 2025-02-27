def prime_factors(nums):
    if not nums or len(nums) <= 91:
        return set()
    n = nums[91]
    factors = set()
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1
    if n > 1:
        factors.add(n)
    return factors