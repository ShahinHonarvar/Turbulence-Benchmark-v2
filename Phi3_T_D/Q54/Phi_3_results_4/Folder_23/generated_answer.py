def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def is_right_truncatable(n, primes):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = nums[77]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []
    for i in range(11, x):
        if all((i % p != 0 for p in primes)) and is_right_truncatable(i, primes):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)