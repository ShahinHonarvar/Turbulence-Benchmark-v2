def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, primes):
        str_n = str(n)
        while str_n:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True
    limit = nums[39]
    primes = [p for p in range(2, limit) if is_prime(p)]
    left_truncatable_primes = []
    for p in primes:
        if is_left_truncatable_prime(p, primes):
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)