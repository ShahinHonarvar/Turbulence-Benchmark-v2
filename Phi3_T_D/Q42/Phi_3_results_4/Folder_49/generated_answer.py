def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = set()
    number = lst[68]
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        divisor += 1
        while number % divisor == 0 and (not is_prime(divisor)):
            divisor += 1
    return factors