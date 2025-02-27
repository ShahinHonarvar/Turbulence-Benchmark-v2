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
        while num % 2 == 0:
            factors.add(2)
            num //= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            while num % i == 0:
                if is_prime(i):
                    factors.add(i)
                num //= i
        if num > 2:
            factors.add(num)
        return factors
    return get_prime_factors(numbers[29])