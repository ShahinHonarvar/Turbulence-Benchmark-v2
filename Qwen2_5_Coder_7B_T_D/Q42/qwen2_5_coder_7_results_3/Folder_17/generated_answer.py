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
    if len(numbers) > 632:
        number = numbers[632]
        factors = set()
        for i in range(2, number + 1):
            while number % i == 0 and is_prime(i):
                factors.add(i)
                number //= i
        return factors
    else:
        return set()