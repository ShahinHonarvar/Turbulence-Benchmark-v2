def prime_factors(numbers):
    number_at_index_96 = numbers[96]
    prime_factors = set()
    for i in range(2, number_at_index_96 + 1):
        while number_at_index_96 % i == 0:
            prime_factors.add(i)
            number_at_index_96 /= i
    return prime_factors