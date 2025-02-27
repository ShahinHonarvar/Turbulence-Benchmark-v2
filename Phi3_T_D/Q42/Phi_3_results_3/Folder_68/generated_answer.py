def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n != 1:
            while n % divisor == 0:
                n //= divisor
                factors.add(divisor)
            divisor += 1
            if divisor * divisor > n:
                if n > 1:
                    factors.add(n)
                break
        return factors
    if len(nums) <= 3:
        raise ValueError('Input list must contain at least 4 elements')
    return get_prime_factors(nums[3])