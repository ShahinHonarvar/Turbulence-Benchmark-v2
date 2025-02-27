def prime_factors(nums):

    def prime_factorize(n):
        factors = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.add(d)
                n //= d
            d += 1
        if n > 1:
            factors.add(n)
        return factors
    if len(nums) > 702:
        n = nums[702]
        return prime_factorize(n)
    else:
        return set()