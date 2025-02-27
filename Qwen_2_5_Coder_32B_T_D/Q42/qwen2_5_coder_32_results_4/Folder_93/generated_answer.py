def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_factors(num):
        factors = set()
        for i in range(2, num + 1):
            if num % i == 0:
                factors.add(i)
        return factors
    target_number = numbers[45]
    factors = get_factors(target_number)
    prime_factors_set = {factor for factor in factors if is_prime(factor)}
    return prime_factors_set