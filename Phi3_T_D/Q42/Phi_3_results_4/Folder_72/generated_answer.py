def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors_of(num):
        primes = set()
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                primes.add(i)
        return primes
    return factors_of(numbers[16]) if len(numbers) > 16 else set()