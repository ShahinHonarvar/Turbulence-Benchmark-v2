def prime_factors(numbers):
    number = numbers[1]
    factors = []
    for i in range(2, number + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    return set(factors)