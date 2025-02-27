def prime_factors(numbers):
    number_at_index_990 = numbers[990]
    for i in range(2, int(number_at_index_990 ** 0.5) + 1):
        while number_at_index_990 % i == 0:
            number_at_index_990 //= i
    return number_at_index_990