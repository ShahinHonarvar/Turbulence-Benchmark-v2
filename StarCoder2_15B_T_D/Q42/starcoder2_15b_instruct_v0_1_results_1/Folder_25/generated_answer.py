def prime_factors(numbers):
    number = numbers[90]
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    factors.append(number)
    return set(factors)