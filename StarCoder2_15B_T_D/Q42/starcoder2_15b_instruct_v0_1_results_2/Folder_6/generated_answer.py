def prime_factors(numbers):
    number_at_index_790 = numbers[790]
    prime_factors = set()
    factor = 2
    while factor * factor <= number_at_index_790:
        while number_at_index_790 % factor == 0:
            prime_factors.add(factor)
            number_at_index_790 //= factor
        factor += 1
    if number_at_index_790 > 1:
        prime_factors.add(number_at_index_790)
    return prime_factors