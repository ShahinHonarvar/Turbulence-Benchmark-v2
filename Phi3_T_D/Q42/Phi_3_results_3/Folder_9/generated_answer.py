def prime_factors(lst):
    n = lst[24]
    factors = set()

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            factors.add(i)
    return factors