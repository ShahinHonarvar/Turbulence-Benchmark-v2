def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factor_set = set()
    num = nums[53]
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            factor_set.add(i)
    return factor_set