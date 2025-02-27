def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_left(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True

    def is_truncatable_right(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def generate_primes():
        primes = []
        for n in range(2, 100000):
            if is_prime(n):
                primes.append(n)
        return primes

    def is_left_right_truncatable(prime):
        return is_truncatable_left(prime) and is_truncatable_right(prime)
    x = numbers[4]
    primes = generate_primes()
    return [p for p in primes if p <= x and is_left_right_truncatable(p)]