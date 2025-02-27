def all_left_truncatable_prime(numbers):

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

    def is_left_truncatable(n):
        if not is_prime(n):
            return False
        while n > 0:
            n = n % 10 ** (len(str(n)) - 1)
            if not is_prime(n):
                return False
        return True
    trunc_primes = [n for n in range(2, numbers[88]) if is_left_truncatable(n)]
    return trunc_primes