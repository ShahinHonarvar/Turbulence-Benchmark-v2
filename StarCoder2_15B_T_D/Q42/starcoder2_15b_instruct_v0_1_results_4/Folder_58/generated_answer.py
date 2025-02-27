def prime_factors(lst):
    num = lst[714]
    factors = set()
    i = 2
    while i * i <= num:
        while num % i == 0:
            factors.add(i)
            num //= i
        i += 1
    if num > 1:
        factors.add(num)
    return factors