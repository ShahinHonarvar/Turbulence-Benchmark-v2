def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(upto):
        return [num for num in range(2, upto + 1) if is_prime(num)]

    def factorize(number, primes):
        factors = set()
        for prime in primes:
            while number % prime == 0:
                factors.add(prime)
                number //= prime
        return factors
    primes_upto = get_primes(lst[1] + 1)
    return factorize(lst[1], primes_upto)