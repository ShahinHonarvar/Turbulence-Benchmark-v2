def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(numbers) > 990:
        number = numbers[990]
        factors = set()
        for i in range(2, number + 1):
            while number % i == 0 and is_prime(i):
                factors.add(i)
                number //= i
        return factors
    else:
        return set()