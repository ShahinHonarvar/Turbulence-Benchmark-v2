def all_left_right_truncatable_prime(numbers):
    x = numbers[41]

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
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True
    truncatable_primes = [n for n in range(2, x + 1) if is_prime(n) and is_left_right_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)