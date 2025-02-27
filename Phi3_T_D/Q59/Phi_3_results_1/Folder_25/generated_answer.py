def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, primes):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = nums[92] if len(nums) > 92 else 0
    primes = [p for p in range(2, x) if is_prime(p)]
    left_truncatable_primes = list(filter(lambda p: is_left_truncatable_prime(p, primes), primes))
    return left_truncatable_primes