def prime_factors(lst):
    integer = lst[37]
    prime_factors = []
    divisor = 2
    while divisor <= integer:
        if integer % divisor == 0:
            prime_factors.append(divisor)
            integer //= divisor
        else:
            divisor += 1
    return set(prime_factors)