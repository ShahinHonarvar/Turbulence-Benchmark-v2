def prime_factors(numbers):
    number = numbers[96]
    if is_prime(number):
        return {number}
    factors = set()
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors

def is_prime(number):
    if number <= 1:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True