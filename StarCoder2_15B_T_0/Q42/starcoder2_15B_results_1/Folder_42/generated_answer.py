def prime_factors(numbers):
    number_at_276 = numbers[276]
    for i in range(2, number_at_276 + 1):
        while number_at_276 % i == 0:
            number_at_276 //= i
    return number_at_276