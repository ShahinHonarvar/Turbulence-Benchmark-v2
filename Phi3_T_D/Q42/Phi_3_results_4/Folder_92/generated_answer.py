from collections import Counter

def prime_factors(nums):

    def prime_factorization(n):
        factors = []
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1
            if divisor * divisor > n:
                if n > 1:
                    factors.append(n)
                    break
        return factors
    if len(nums) > 0 and all((isinstance(x, int) and x > 0 for x in nums)):
        first_num = nums[0]
        return set(prime_factorization(first_num))
    return set()