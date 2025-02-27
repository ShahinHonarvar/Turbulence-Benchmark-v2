def prime_factors(numbers):
    number_at_47 = numbers[47]
    for i in range(2, number_at_47 + 1):
        while number_at_47 % i == 0:
            number_at_47 //= i
    return number_at_47