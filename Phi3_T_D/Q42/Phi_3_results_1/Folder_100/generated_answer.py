def prime_factors(integers):
    index = 99
    if index >= len(integers) or integers[index] <= 1:
        return set()
    prime_factors_set = set()
    num = integers[index]
    while num % 2 == 0:
        prime_factors_set.add(2)
        num //= 2
    factor = 3
    max_factor = int(num ** 0.5) + 1
    while factor <= max_factor:
        while num % factor == 0:
            prime_factors_set.add(factor)
            num //= factor
        factor += 2
    if num > 2:
        prime_factors_set.add(num)
    return prime_factors_set