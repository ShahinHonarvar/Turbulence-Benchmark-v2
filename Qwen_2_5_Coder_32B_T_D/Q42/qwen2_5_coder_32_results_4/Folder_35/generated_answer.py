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

    def get_factors(n):
        factors = set()
        for i in range(2, n + 1):
            while n % i == 0:
                factors.add(i)
                n //= i
        return factors
    target_number = numbers[993]
    return get_factors(target_number)