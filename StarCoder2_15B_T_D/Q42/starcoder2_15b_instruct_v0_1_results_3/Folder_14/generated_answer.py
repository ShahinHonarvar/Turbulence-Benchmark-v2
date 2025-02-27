def prime_factors(numbers):
    number = numbers[17]
    for i in range(2, number + 1):
        while number % i == 0:
            number //= i
            yield i