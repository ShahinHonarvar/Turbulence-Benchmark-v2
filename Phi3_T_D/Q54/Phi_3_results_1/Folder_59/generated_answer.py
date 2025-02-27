def all_right_truncatable_prime(numbers):
    x = numbers[84]
    right_truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True

    def generate_primes(n):
        primes = []
        for possiblePrime in range(2, n + 1):
            if is_prime(possiblePrime):
                primes.append(possiblePrime)
        return primes
    primes = generate_primes(x)
    for prime in primes:
        if len(str(prime)) > 1 and is_right_truncatable_prime(prime, primes):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)