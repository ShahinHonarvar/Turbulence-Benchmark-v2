def prime_factors(numbers):
    number = numbers[96]
    factors = []
    i = 2
    while i * i <= number:
        while number % i == 0:
            factors.append(i)
            number //= i
        i += 1
    if number > 1:
        factors.append(number)
    return set(factors)