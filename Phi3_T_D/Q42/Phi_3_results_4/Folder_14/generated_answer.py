def prime_factors(numbers):

    def get_primes_up_to_n(n):
        primes = []
        for num in range(2, n + 1):
            prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                primes.append(num)
        return primes

    def prime_factors_of(n, primes):
        factors = set()
        for prime in primes:
            while n % prime == 0:
                factors.add(prime)
                n //= prime
        return factors
    if len(numbers) > 17:
        primes = get_primes_up_to_n(numbers[17])
        factors = prime_factors_of(numbers[17], primes)
        return factors
    return set()