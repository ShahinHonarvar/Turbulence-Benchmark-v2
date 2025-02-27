def prime_factors(lst):
    num = lst[263]
    factors = []
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 1:
        factors.append(num)
    return set(factors)