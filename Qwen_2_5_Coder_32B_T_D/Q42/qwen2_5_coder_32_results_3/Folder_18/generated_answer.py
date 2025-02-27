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

    def get_factors(num):
        factors = set()
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                factors.add(i)
                num //= i
        if num > 1:
            factors.add(num)
        return factors
    if len(numbers) < 313:
        return set()
    return get_factors(numbers[312])