def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if not n:
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    truncatable_primes = [n for n in range(2, nums[36]) if is_left_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)