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
    factors = set()
    num = lst[702]
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0 and is_prime(divisor):
            factors.add(divisor)
            while num % divisor == 0:
                num //= divisor
        divisor += 1
    if num > 1:
        factors.add(num)
    return factors