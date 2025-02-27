def prime_factors(nums):
    n = nums[993]
    prime_factors = set()
    i = 2
    while i * i <= n:
        while n % i == 0:
            prime_factors.add(i)
            n //= i
        i += 1
    if n > 1:
        prime_factors.add(n)
    return prime_factors