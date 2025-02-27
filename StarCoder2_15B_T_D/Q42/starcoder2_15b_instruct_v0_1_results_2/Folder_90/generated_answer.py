def prime_factors(lst):
    num = lst[263]
    factors = set()
    for i in range(2, num + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    return factors