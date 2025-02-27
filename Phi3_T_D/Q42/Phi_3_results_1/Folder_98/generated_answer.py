def prime_factors(num_list):
    num = num_list[3] if len(num_list) > 3 else None
    if num is None:
        return 'List must contain at least 5 integers.'
    factors = set()
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        divisor += 1
    return factors