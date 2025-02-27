def prime_factors(numbers):

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

    def get_primes_up_to(n):
        primes = []
        for num in range(2, n + 1):
            if is_prime(num):
                primes.append(num)
        return primes

    def prime_factors_of(n):
        factors = set()
        primes = get_primes_up_to(int(n ** 0.5) + 1)
        for prime in primes:
            while n % prime == 0:
                factors.add(prime)
                n //= prime
        if n > 1:
            factors.add(n)
        return factors
    return prime_factors_of(numbers[276])