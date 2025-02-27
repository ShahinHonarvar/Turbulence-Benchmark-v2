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

def prime_factors(lst):
    if len(lst) > 10:
        num = lst[10]
        factors = set()
        for i in range(2, num + 1):
            if is_prime(i) and num % i == 0:
                factors.add(i)
        return factors
    return set()