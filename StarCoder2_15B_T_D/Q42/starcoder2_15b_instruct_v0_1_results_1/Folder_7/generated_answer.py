def prime_factors(numbers):
    number = numbers[851]
    i = 2
    prime_factors = []
    while i * i <= number:
        while number % i == 0:
            prime_factors.append(i)
            number /= i
        i += 1
    if number > 1:
        prime_factors.append(number)
    return set(prime_factors)