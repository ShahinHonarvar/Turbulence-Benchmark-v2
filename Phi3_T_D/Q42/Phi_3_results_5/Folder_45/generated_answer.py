def prime_factors(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    factors = set()
    while lst[33] % 2 == 0:
        factors.add(2)
        lst[33] //= 2
    for i in range(3, int(lst[33] ** 0.5) + 1, 2):
        while lst[33] % i == 0:
            factors.add(i)
            lst[33] //= i
    if lst[33] > 2:
        factors.add(lst[33])
    return factors