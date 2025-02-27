def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_primes(n):
        primes = set()
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                primes.add(i)
        return primes
    return find_primes(nums[49]) if len(nums) > 49 else set()