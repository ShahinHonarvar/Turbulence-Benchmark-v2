def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True
    x = nums[22]
    right_truncatable_primes = [n for n in range(2, x) if is_right_truncatable(n)]
    return sorted(right_truncatable_primes, reverse=True)