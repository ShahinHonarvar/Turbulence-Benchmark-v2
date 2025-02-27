def prime_factors(lst):
    number = lst[65]
    factors = set()

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            factors.add(i)
    return factors