def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = numbers[42]
    factors = set()
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            if is_prime(divisor):
                factors.add(divisor)
            num //= divisor
        divisor += 1
    return factors