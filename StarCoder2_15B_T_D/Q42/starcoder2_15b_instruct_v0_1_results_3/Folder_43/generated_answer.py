def prime_factors(numbers):
    number_at_29 = numbers[29]
    prime_factors = set()
    i = 2
    while i * i <= number_at_29:
        if number_at_29 % i == 0:
            prime_factors.add(i)
            number_at_29 //= i
        else:
            i += 1
    prime_factors.add(number_at_29)
    return prime_factors