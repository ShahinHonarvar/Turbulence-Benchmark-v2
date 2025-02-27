def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while divisor * divisor <= n:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
        if n > 1:
            factors.add(n)
        return factors
    index_48 = numbers[48]
    if index_48 < 0:
        raise ValueError('Index 48 is out of range')
    return get_prime_factors(index_48)