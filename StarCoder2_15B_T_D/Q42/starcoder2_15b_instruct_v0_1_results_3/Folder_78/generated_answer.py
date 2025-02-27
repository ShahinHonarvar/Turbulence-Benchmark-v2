def prime_factors(numbers):
    number = numbers[91]
    factors = set()
    for i in range(2, number + 1):
        while number % i == 0:
            factors.add(i)
            number //= i
    return factors