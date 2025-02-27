def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors_set(n):
        factors = set()
        for i in range(2, n + 1):
            if is_prime(i) and n % i == 0:
                factors.add(i)
        return factors
    return factors_set(nums[15])