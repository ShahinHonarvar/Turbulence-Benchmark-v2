def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of_number(n):
        factors = set()
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.add(divisor)
                n /= divisor
            divisor += 1
        return factors
    if len(numbers) > 76:
        return prime_factors_of_number(numbers[77])
    raise IndexError('The list does not have an item at index 77')