def prime_factors(lst):
    num = lst[90]
    prime_factors = []
    div = 2
    while div * div <= num:
        while num % div == 0:
            prime_factors.append(div)
            num //= div
        div += 1
    if num > 1:
        prime_factors.append(num)
    return set(prime_factors)