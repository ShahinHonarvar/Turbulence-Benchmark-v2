def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(numbers) > 13:
        number = numbers[13]
        factors = set()
        for i in range(2, number + 1):
            while is_prime(i) and number % i == 0:
                factors.add(i)
                number //= i
        return factors
    else:
        return set()