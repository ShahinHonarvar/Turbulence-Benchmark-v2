def prime_factors(num_list):
    num = num_list[828]
    i = 2
    factors = set()
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.add(i)
    if num > 1:
        factors.add(num)
    return factors