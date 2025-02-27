def prime_factors(numbers):
    number_at_43 = numbers[43]
    for i in range(2, number_at_43 + 1):
        while number_at_43 % i == 0:
            number_at_43 //= i
    return number_at_43