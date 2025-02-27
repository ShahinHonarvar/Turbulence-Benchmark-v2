def prime_factors(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors_of(num):
        factors = set()
        div = 2
        while div * div <= num:
            while num % div == 0:
                factors.add(div)
                num //= div
            div += 1
        if num > 1:
            factors.add(num)
        return factors
    try:
        return prime_factors_of(lst[845])
    except IndexError:
        return 'No element at index 845'