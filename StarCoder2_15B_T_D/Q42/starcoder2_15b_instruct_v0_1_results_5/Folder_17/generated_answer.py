def prime_factors(numbers):
    number = numbers[632]
    result = set()
    for i in range(2, number + 1):
        while number % i == 0:
            result.add(i)
            number //= i
    return result