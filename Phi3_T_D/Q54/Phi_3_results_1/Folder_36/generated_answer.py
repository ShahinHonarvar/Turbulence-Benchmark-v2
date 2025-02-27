def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes_set):
        if n == 0:
            return True
        if not is_prime(n):
            return False
        return is_right_truncatable_prime(n // 10, primes_set)
    truncable_primes = set()
    for num in range(nums[992]):
        for i in range(num, 9, -1):
            if is_right_truncatable_prime(i, truncable_primes):
                truncable_primes.add(i)
        if len(truncable_primes) > 0:
            break
    return sorted(list(truncable_primes))