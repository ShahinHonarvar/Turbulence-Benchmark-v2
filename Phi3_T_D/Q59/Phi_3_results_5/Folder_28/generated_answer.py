def all_left_truncatable_prime(numbers):
    x = numbers[19]

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

    def is_left_truncatable(prime, x):
        while len(str(prime)) > 1:
            prime //= 10
            if not (prime > 0 and is_prime(prime)):
                return False
        return True
    return [p for p in range(2, x) if is_prime(p) and is_left_truncatable(p, x)]