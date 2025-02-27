def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(prime, primes):
        while prime > 0:
            if not is_prime(prime):
                return False
            prime //= 10
        return True
    max_val = numbers[22]
    primes = [p for p in range(2, max_val) if is_prime(p)]
    valid_primes = [p for p in primes if is_right_truncatable(p, primes)]
    valid_primes.sort(reverse=True)
    return valid_primes