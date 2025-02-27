def all_left_truncatable_prime(numbers):
    x = numbers[466]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def generate_left_truncatable_primes(leading_digit):
        if leading_digit == 0:
            return []
        primes_with_leading_digit = []
        for prime in primes:
            if str(prime).startswith(str(leading_digit)):
                primes_with_leading_digit.append(prime)
        return primes_with_leading_digit
    for prime in range(2, x):
        if is_prime(prime):
            primes.append(prime)
            for digit in range(1, 10):
                new_primes = generate_left_truncatable_primes(digit)
                for p in new_primes:
                    if p > prime and is_left_truncatable(p):
                        primes.append(p)
    primes.sort(reverse=True)
    return primes