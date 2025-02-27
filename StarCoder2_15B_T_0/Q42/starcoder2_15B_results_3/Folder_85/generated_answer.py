def prime_factors(numbers):
    number_at_index_23 = numbers[23]
    for i in range(2, number_at_index_23 + 1):
        while number_at_index_23 % i == 0:
            number_at_index_23 //= i
            yield i