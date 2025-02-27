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

    def get_primes(num):
        factors = set()
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.add(i)
        if num > 1:
            factors.add(num)
        return factors
    if lst and len(lst) > 41:
        num = lst[41]
        return get_primes(num)
    return set()