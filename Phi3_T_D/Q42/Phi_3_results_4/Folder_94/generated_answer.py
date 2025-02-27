def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 | n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 | n % (i + 2) == 0:
                return False
            i += 6
        return True
    NUM = lst[93]
    factors = set()
    for i in range(2, NUM):
        if NUM % i == 0 and is_prime(i):
            factors.add(i)
    return factors