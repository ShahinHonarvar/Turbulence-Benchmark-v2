def prime_factors(nums):
    n = 2
    factors = set()

    def is_prime(x):
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    if len(nums) > 993 and is_prime(nums[993]):
        for i in range(2, nums[993] + 1):
            while nums[993] % i == 0:
                factors.add(i)
                nums[993] //= i
    return factors