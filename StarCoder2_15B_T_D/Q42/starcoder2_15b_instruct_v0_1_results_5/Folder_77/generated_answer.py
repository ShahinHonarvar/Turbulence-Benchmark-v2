def prime_factors(numbers):
    number = numbers[985]
    i = 2
    prime_factors = set()
    while i * i <= number:
        while number % i == 0:
            prime_factors.add(i)
            number //= i
        i += 1
    if number > 1:
        prime_factors.add(number)
    return prime_factors