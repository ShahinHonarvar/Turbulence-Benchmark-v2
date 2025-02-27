def all_left_right_truncatable_prime(nums):

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

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if int(str_n[i:]) not in primes or int(str_n[:i + 1]) not in primes:
                return False
        return True
    x = nums[78]
    primes = {i for i in range(2, x + 1) if is_prime(i)}
    truncatable_primes = [p for p in primes if is_left_right_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)