def prime_factors(numbers):
    number_at_49 = numbers[49]
    for i in range(2, number_at_49 + 1):
        while number_at_49 % i == 0:
            number_at_49 //= i
    return number_at_49