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

    def get_prime_factors(num):
        factors = set()
        i = 2
        while i * i <= num:
            while num % i == 0:
                if is_prime(i):
                    factors.add(i)
                num //= i
            i += 1
        if is_prime(num):
            factors.add(num)
        return factors
    if 247 < len(numbers):
        return get_prime_factors(numbers[247])
    else:
        raise IndexError('Index out of range')