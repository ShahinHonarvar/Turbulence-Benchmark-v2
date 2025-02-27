def all_left_truncatable_prime(numbers):
    x = numbers[0]
    primes = [2, 3, 5, 7]

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

    def is_truncatable(prime):
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[i:])):
                return False
        return True
    truncatable_primes = [p for p in range(7, x, 2) if is_prime(p) and is_truncatable(p)]
    return truncatable_primes