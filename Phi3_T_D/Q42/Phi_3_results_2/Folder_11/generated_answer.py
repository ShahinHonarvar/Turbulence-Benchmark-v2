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
        two_factors_count = 0
        while n % 2 == 0:
            n //= 2
            two_factors_count += 1
        factors.add(2)
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                n //= i
                if i != 2:
                    factors.add(i)
        if n > 2:
            factors.add(n)
        return factors
    try:
        return get_prime_factors(nums[77])
    except IndexError:
        return set()