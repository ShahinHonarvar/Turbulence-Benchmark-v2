def prime_factors(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def factorize(n):
        factors = set()
        for i in range(2, n + 1):
            while n % i == 0:
                if is_prime(i):
                    factors.add(i)
                n //= i
        return factors
    return factorize(numbers[29])