def prime_factors(numbers):
    number = numbers[985]
    prime_factors = set()
    for i in range(2, number + 1):
        while number % i == 0:
            prime_factors.add(i)
            number //= i
    return prime_factors