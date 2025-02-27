def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        result = set()
        for i in range(2, n + 1):
            while n % i == 0 and is_prime(i):
                result.add(i)
                n //= i
        return result
    if len(nums) >= 74:
        return factors(nums[73])
    else:
        return set()