def prime_factors(numbers):
    number = numbers[54]
    factors = []
    i = 2
    while i <= number:
        if number % i == 0:
            factors.append(i)
            number //= i
        else:
            i += 1
    prime_factors = set(factors)
    return prime_factors