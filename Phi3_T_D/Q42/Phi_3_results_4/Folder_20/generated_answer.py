def prime_factors(numbers):

    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def get_prime_factors(number):
        factors = set()
        for i in range(2, number + 1):
            while number % i == 0 and is_prime(i):
                factors.add(i)
                number //= i
        return factors
    if 53 < len(numbers):
        number_at_53 = numbers[53]
        return get_prime_factors(number_at_53)
    else:
        raise ValueError('List must contain at least 54 integers')