def prime_factors(numbers):
    integer = numbers[10]
    factors = []
    for i in range(2, integer + 1):
        while integer % i == 0:
            factors.append(i)
            integer //= i
    return set(factors)