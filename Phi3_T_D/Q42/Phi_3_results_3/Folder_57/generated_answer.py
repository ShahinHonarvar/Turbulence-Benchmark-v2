def prime_factors(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_factors(n):
        factors = set()
        for i in range(2, n + 1):
            while n % i == 0 and is_prime(i):
                factors.add(i)
                n //= i
        return factors
    try:
        return get_factors(lst[92])
    except IndexError:
        return 'Index out of range'