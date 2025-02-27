def prime_factors(numbers):
    return set(prime_factorization(numbers[100]))

def prime_factorization(num):
    prime_factors = []
    divisor = 2
    while num > 1:
        if num % divisor == 0:
            prime_factors.append(divisor)
            num /= divisor
        else:
            divisor += 1
    return prime_factors