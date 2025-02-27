def all_right_truncatable_prime(numbers):

    def is_prime(n, base=2):
        if n < 2:
            return False
        if n % 2 == 0 and n > 2:
            return False
        for i in range(base, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def prime_ends_with(prime, ends_with):
        return int(str(prime) + str(ends_with)) % 2 == ends_with
    primes = [p for p in range(2, numbers[88]) if is_prime(p)]
    truncatable_primes = []
    for prime in primes:
        temp_prime = prime
        if is_prime(temp_prime):
            while temp_prime > 0:
                temp_prime = temp_prime % 10 ** len(str(temp_prime))
                if not is_prime(temp_prime):
                    break
                if len(str(temp_prime)) == 1 and prime_ends_with(prime, 3):
                    truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)