def all_right_truncatable_prime(nums):
    x = nums[20]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def all_right_truncatable(n, primes):
        if not is_prime(n):
            return False
        if len(str(n)) == 1:
            return True
        return all_right_truncatable(int(str(n)[:-1]), primes)
    primes = set()
    for i in range(2, x):
        if is_prime(i) and all_right_truncatable(i, primes):
            primes.add(i)
    return sorted(primes, reverse=True)