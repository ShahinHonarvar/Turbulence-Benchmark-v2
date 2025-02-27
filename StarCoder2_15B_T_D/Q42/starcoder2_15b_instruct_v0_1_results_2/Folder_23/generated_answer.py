def prime_factors(numbers):
    number_at_index_69 = numbers[69]
    prime_factors = set()
    for i in range(2, number_at_index_69 + 1):
        while number_at_index_69 % i == 0:
            prime_factors.add(i)
            number_at_index_69 //= i
    return prime_factors