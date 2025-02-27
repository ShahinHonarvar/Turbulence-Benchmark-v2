def prime_factors(numbers):
    number = numbers[53]
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number