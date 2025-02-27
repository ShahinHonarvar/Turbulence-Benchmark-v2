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

    def get_primes(n):
        primes = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                primes.add(i)
                n //= i
            else:
                i += 1
        if n > 1:
            primes.add(n)
        return primes
    return get_primes(numbers[87]) if 87 < len(numbers) else set()