def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors = set()
    for i in range(2, nums[0] + 1):
        if is_prime(i) and nums[0] % i == 0:
            prime_factors.add(i)
    return prime_factors