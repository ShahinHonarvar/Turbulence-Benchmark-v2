def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    number = lst[926]
    factors = set()
    d = 2
    while d * d <= number:
        while number % d == 0:
            factors.add(d)
            number //= d
        d += 1
    if number > 1:
        factors.add(number)
    return factors