def prime_factors(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n, divisor=2):
        while n % divisor == 0 and n > 1:
            if is_prime(divisor):
                result.add(divisor)
            n //= divisor
        if n > 1:
            factors(n, divisor + 1)
    result = set()
    if len(nums) > 66:
        factors(nums[66], 2)
    return result