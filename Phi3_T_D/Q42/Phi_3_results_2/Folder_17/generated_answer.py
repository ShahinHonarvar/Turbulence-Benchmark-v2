def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    if len(lst) <= 632:
        return 'Index out of range'

    def find_factors(n, factors):
        for j in range(2, n // 2 + 1):
            if n % j == 0:
                if is_prime(j):
                    factors.add(j)
                    return find_factors(n // j, factors)
        if is_prime(n):
            factors.add(n)
        return factors
    return find_factors(lst[632], set())