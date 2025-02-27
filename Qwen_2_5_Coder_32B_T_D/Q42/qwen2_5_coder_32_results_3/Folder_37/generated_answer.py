def prime_factors(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_factors(num):
        factors = set()
        for i in range(2, num + 1):
            if num % i == 0:
                factors.add(i)
        return factors

    def prime_factors_of(num):
        factors = get_factors(num)
        return {factor for factor in factors if is_prime(factor)}
    if len(lst) > 28:
        return prime_factors_of(lst[28])
    return set()