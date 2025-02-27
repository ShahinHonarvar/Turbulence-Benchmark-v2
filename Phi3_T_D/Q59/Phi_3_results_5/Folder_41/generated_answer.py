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
            n = n % 10 ** (len(str(n)) - 1)
        return True
    x = nums[46]
    primes = [2, 3, 5, 7]
    for i in range(11, x, 2):
        if is_prime(i):
            primes.append(i)
    left_truncatable_primes = [p for p in primes if is_left_truncatable_prime(p, primes)]
    return sorted(left_truncatable_primes, reverse=True)