def all_right_truncatable_prime(nums):
    x = nums[30]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if is_prime(int(str_n[i:])) is False:
                return False
        return True
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatable_primes = [p for p in primes if is_right_truncatable(p)]
    return sorted(truncatable_primes, reverse=True)