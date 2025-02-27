def prime_factors(lst):
    if not lst or len(lst) < 91:
        return set()
    num = lst[90]
    factors = set()
    while num % 2 == 0:
        factors.add(2)
        num //= 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 2:
        factors.add(num)
    return factors