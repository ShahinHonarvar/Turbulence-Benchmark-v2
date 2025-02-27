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

    def factors(n):
        result = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                result.update([i, n // i])
        return result

    def prime_factors_set(n):
        nonlocal primes
        result = set()
        for f in factors(n):
            if f in primes:
                result.add(f)
            else:
                result.update(prime_factors_set(f))
        if is_prime(n):
            result.add(n)
        return result
    primes = set(filter(is_prime, range(2, int(max(numbers) ** 0.5) + 1)))
    return prime_factors_set(numbers[993])