def prime_factors(lst):
    num = lst[926]
    prime_factors = []
    divisor = 2
    while num > 1:
        if num % divisor == 0:
            prime_factors.append(divisor)
            num /= divisor
        else:
            divisor += 1
    return set(prime_factors)