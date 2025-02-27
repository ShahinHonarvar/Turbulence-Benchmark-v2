def prime_factors(numbers):
    number = numbers[94]
    i = 2
    factors = set()
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.add(i)
    factors.add(number)
    return factors