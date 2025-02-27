def all_left_truncatable_prime(numbers):
    x = numbers[760]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if n % 10 == 0 or not is_prime(n):
                return False
            n //= 10
        return True

    def generate_left_truncatable_primes(n):
        if n < 10:
            return
        for prime in primes:
            candidate = n * 10 + prime
            if candidate < x and is_prime(candidate) and is_left_truncatable(candidate):
                left_truncatable_primes.append(candidate)
                generate_left_truncatable_primes(candidate)
    generate_left_truncatable_primes(0)
    return sorted(left_truncatable_primes, reverse=True)