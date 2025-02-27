def prime_factors(integers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    factors = set()
    candidate = 2
    target = integers[4]
    while target > 1:
        if target % candidate == 0 and is_prime(candidate):
            factors.add(candidate)
            while target % candidate == 0:
                target //= candidate
        candidate += 1
    return factors