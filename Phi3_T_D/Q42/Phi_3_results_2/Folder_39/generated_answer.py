def prime_factors(nums):

    def prime_factors_of_number(n):
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
    if len(nums) > 59:
        return prime_factors_of_number(nums[59])
    raise IndexError('The provided list must contain at least 60 elements.')