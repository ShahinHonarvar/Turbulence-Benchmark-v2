def all_left_truncatable_prime(values):
    x = values[4]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, digits):
        if not is_prime(n):
            return False
        if n < x:
            left_truncatable_primes.append(n)
        if len(digits) > 1 and is_prime(n // 10):
            return is_left_truncatable_prime(n // 10, digits[:-1]) or is_left_truncatable_prime(n, digits[:-1])
        return n % 10 > 0
    for number in range(23, x):
        if is_left_truncatable_prime(number, str(number)):
            if number not in left_truncatable_primes:
                left_truncatable_primes.append(number)
    return left_truncatable_primes