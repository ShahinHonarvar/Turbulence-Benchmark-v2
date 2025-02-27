def prime_factors(numbers):
    number_at_37 = numbers[37]
    prime_factors = set()
    for i in range(2, number_at_37 + 1):
        while number_at_37 % i == 0:
            prime_factors.add(i)
            number_at_37 //= i
    return prime_factors