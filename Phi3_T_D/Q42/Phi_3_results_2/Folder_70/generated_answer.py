def prime_factors(lst):

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

    def prime_factorization(n):
        factors = set()
        divisor = 2
        while n >= 2:
            if n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            else:
                divisor += 1
            if is_prime(n):
                factors.add(n)
                break
        return factors
    if len(lst) > 845:
        return prime_factorization(lst[845])
    else:
        raise IndexError(f'List index out of range. Length of the list is {len(lst)}, cannot access index 845.')