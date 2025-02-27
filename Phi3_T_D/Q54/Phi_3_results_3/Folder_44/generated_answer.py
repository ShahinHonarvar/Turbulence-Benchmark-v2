def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def is_right_truncatable_prime(n, primes):
        if n < 10 or not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[:i])):
                return False
        return True
    x = nums[39]
    primes = []
    for n in range(2, x):
        if is_right_truncatable_prime(n, primes):
            primes.append(n)
    return sorted(primes)