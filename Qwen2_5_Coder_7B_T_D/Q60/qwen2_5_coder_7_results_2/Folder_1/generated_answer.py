def all_left_right_truncatable_prime(numbers):
    x = numbers[20]

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

    def is_left_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:-i - 1])):
                return False
        return True
    truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)