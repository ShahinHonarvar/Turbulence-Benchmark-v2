def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def prime_factors_of(number):
        factors = set()
        while number % 2 == 0:
            factors.add(2)
            number //= 2
        for i in range(3, int(number ** 0.5) + 1, 2):
            while number % i == 0:
                factors.add(i)
                number //= i
        if number > 2:
            factors.add(number)
        return factors
    if len(numbers) > 7:
        return prime_factors_of(numbers[7])
    else:
        raise ValueError('The list must have at least 8 elements.')