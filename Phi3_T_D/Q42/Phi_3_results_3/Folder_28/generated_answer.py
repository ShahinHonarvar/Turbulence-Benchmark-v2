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
        divisor = 2
        while divisor * divisor <= num:
            while num % divisor == 0:
                factors.add(divisor)
                num //= divisor
            divisor += 1
        if num > 1:
            factors.add(num)
        return factors
    if 37 < len(numbers):
        prime_factors_set = get_prime_factors(numbers[37])
        return prime_factors_set
    else:
        return 'Index is out of range.'