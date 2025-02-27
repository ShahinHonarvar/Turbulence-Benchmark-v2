def prime_factors(numbers):
    num = numbers[47]
    factors = []
    i = 2
    while i <= num:
        if num % i == 0:
            factors.append(i)
            num //= i
        else:
            i += 1
    return set(factors)