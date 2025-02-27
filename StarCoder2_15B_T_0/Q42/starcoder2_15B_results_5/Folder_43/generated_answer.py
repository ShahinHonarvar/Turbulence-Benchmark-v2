def prime_factors(numbers):
    number_at_29 = numbers[29]
    for i in range(2, number_at_29 + 1):
        while number_at_29 % i == 0:
            number_at_29 //= i
    return number_at_29