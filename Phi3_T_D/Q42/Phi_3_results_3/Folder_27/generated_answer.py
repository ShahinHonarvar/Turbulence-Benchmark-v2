def prime_factors(numbers):
    num = numbers[56]
    prime_factors_set = set()
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            prime_factors_set.add(divisor)
            num //= divisor
        divisor += 1
    return prime_factors_set