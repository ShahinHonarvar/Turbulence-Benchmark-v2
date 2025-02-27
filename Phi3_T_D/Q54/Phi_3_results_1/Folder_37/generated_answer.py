def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes):
        if n not in primes:
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    primes_set = set()
    for num in range(2, nums[35]):
        if is_prime(num):
            primes_set.add(num)
    right_truncatable_primes = [p for p in primes_set if is_right_truncatable_prime(p, primes_set)]
    return sorted(right_truncatable_primes, reverse=True)