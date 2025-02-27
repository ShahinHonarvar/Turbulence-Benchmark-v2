def prime_factors(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_factors(num):
        factors = set()
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.add(i)
                factors.add(num // i)
        return factors
    num = numbers[849]
    factors = get_factors(num)
    prime_factors = {factor for factor in factors if is_prime(factor)}
    return prime_factors