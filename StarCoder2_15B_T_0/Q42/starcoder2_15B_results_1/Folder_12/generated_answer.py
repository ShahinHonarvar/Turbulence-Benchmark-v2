def prime_factors(numbers):
    number_at_27 = numbers[27]
    for i in range(2, number_at_27 + 1):
        while number_at_27 % i == 0:
            number_at_27 //= i
    return number_at_27