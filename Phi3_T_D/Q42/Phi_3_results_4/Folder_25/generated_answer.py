def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors_list(n):
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    primes = set()
    if len(numbers) > 90:
        nth_number = numbers[90]
        if is_prime(nth_number):
            primes.add(nth_number)
        else:
            factors = factors_list(nth_number)
            for p in factors:
                if is_prime(p):
                    primes.add(p)
    return primes