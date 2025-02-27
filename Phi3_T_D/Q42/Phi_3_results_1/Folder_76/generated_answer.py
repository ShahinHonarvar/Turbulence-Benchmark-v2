def prime_factors(nums):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def factors(n):
        return {i for i in range(2, n + 1) if is_prime(i) and n % i == 0}
    return factors(nums[537])