def prime_factors(numbers):
    number = numbers[685]
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            number //= i
    return number