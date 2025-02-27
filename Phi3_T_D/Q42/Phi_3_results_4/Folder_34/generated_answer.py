def prime_factors(int_list):
    target_int = int_list[97]
    factors = set()
    divisor = 2
    while divisor * divisor <= target_int:
        while target_int % divisor == 0:
            factors.add(divisor)
            target_int //= divisor
        divisor += 1
    if target_int > 1:
        factors.add(target_int)
    return factors