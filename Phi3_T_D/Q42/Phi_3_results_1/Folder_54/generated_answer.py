def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        return {x for x in range(2, n // 2 + 1) if n % x == 0 and is_prime(x)}
    return factors(nums[51])