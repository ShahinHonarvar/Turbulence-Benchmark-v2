def prime_factors(lst):
    num = lst[28]
    factors = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return factors