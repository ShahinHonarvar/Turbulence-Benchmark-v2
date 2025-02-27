def prime_factors(numbers):
    num = numbers[17]
    i = 2
    factors = set()
    while i <= num:
        while num % i == 0:
            factors.add(i)
            num //= i
        i += 1
    return factors