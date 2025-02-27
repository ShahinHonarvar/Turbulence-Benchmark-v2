def all_left_right_truncatable_prime(nums):
    x = nums[41]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
            if '0' in str_n[:i + 1]:
                return False
        return True
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = [p for p in primes if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)