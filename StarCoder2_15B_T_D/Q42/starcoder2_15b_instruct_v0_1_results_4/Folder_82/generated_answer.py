def prime_factors(numbers):
    number = numbers[83]
    factors = set()
    i = 2
    while i * i <= number:
        while number % i == 0:
            factors.add(i)
            number //= i
        i += 1
    if number > 1:
        factors.add(number)
    return factors