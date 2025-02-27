def prime_factors(nums):

    def prime_factorisation(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    return prime_factorisation(nums[42]) if 42 < len(nums) else set()