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

    def get_prime_factors(num):
        factors = set()
        d = 2
        while d * d <= num:
            while num % d == 0:
                if is_prime(d):
                    factors.add(d)
                num //= d
            d += 1
        if num > 1 and is_prime(num):
            factors.add(num)
        return factors
    return get_prime_factors(numbers[33])