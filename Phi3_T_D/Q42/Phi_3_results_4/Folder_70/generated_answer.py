def prime_factors(numbers):
    factors = []
    prime_number = numbers[845]
    divisor = 2
    while divisor * divisor <= prime_number:
        if prime_number % divisor:
            divisor += 1
        else:
            prime_number //= divisor
            factors.append(divisor)
    if prime_number > 1:
        factors.append(prime_number)
    return set(factors)