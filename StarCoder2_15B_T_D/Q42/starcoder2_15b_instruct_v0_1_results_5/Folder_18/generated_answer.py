def prime_factors(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = nums[312]
    return {factor for factor in range(2, num + 1) if is_prime(factor) and num % factor == 0}