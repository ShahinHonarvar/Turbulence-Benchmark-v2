def prime_factors(lst):
    if len(lst) < 61 or not isinstance(lst, list) or (not all((isinstance(i, int) and i > 0 for i in lst))):
        raise ValueError('Input must be a list of positive integers with at least 61 elements.')

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors_of_num(num):
        factors = set()
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor:
                divisor += 1
            else:
                num //= divisor
                factors.add(divisor)
        if num > 1:
            factors.add(num)
        return factors
    return prime_factors_of_num(lst[60])