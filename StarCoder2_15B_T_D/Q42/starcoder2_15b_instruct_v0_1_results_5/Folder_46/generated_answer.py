def prime_factors(numbers):
    prime_factors = []
    number = numbers[453]
    for i in range(2, number + 1):
        while number % i == 0:
            prime_factors.append(i)
            number //= i
    return set(prime_factors)