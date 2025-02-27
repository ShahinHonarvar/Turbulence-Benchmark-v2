def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable_prime(n):
        s = str(n)
        while s:
            if not is_prime(int(s)) or '0' in s:
                return False
            s = s[1:]
        return True
    x = nums[7]
    primes = [n for n in range(2, x) if is_prime(n)]
    left_truncatable_primes = [n for n in primes if is_left_truncatable_prime(n)]
    return sorted(left_truncatable_primes)