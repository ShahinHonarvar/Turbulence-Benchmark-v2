def prime_factors(numbers):
    number = numbers[59]
    for i in range(2, number + 1):
        while number % i == 0:
            number /= i
    return i