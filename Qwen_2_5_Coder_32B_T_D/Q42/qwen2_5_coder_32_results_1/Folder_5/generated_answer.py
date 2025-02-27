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
        f = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                f.add(i)
                f.add(n // i)
        return f

    def prime_factors_set(n):
        return {p for p in factors(n) if is_prime(p)}
    return prime_factors_set(numbers[67])