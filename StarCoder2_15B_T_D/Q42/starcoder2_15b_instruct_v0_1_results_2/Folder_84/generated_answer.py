def prime_factors(numbers):
    number_at_index_685 = numbers[685]
    for i in range(2, number_at_index_685 + 1):
        while number_at_index_685 % i == 0:
            number_at_index_685 //= i
            if number_at_index_685 == 1:
                return i