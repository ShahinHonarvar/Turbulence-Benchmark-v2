def all_left_right_truncatable_prime(x):
    x = x[36]

    def is_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        if num % 10 == 0 or not is_prime(num):
            return False
        return is_truncatable_prime(num // 10)

    def is_prime(num):
        if num < 2:
            return False
        if num in (2, 3):
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(num ** 0.5) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(10, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)