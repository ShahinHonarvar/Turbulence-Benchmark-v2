def prime_factors(numbers):
    number = numbers[194]
    i = 2
    factors = set()
    while i * i <= number:
        while number % i == 0:
            factors.add(i)
            number //= i
        i += 1
    if number > 1:
        factors.add(number)
    return factors