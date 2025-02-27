def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        for i in range(2, num + 1):
            if is_prime(i) and num % i == 0:
                factors.add(i)
        return factors
    if len(numbers) > 83:
        return get_prime_factors(numbers[83])
    else:
        return 'Index out of range'