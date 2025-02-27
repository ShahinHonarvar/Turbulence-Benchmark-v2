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
        while n > 1:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
            if divisor * divisor > n:
                if n > 1 and is_prime(n):
                    factors.add(n)
                    break
        return factors
    if len(numbers) <= 74:
        return None
    number_to_factor = numbers[74]
    return get_prime_factors(number_to_factor)