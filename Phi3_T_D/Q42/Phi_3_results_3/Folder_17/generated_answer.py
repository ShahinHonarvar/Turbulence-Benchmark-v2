def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    num = numbers[632]
    factors = set()
    divisor = 2
    while num >= divisor:
        if num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        else:
            divisor += 1
    prime_factors = set(filter(is_prime, factors))
    return prime_factors