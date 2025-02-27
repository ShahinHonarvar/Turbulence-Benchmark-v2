def prime_factors(integers):
    number = integers[63]
    factors = set()

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        divisor += 1
        if divisor * divisor > number:
            if number > 1:
                factors.add(number)
                break
    return factors