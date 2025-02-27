def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factorize(n):
        factors = set()
        divisor = 2
        while divisor <= n:
            if n % divisor == 0 and is_prime(divisor):
                factors.add(divisor)
                n //= divisor
            else:
                divisor += 1
        return factors
    if len(lst) > 59:
        return factorize(lst[59])
    else:
        raise IndexError('List index out of range')