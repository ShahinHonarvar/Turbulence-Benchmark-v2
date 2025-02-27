def prime_factors(numbers):
    number_at_57 = numbers[57]
    for i in range(2, number_at_57 + 1):
        while number_at_57 % i == 0:
            number_at_57 //= i
    return number_at_57