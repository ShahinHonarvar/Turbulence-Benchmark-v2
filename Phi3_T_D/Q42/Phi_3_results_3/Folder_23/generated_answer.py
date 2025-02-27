def prime_factors(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors_of_num(num):
        factors = set()
        for i in range(2, num + 1):
            if is_prime(i) and num % i == 0:
                factors.add(i)
        return factors
    if len(lst) > 69:
        return prime_factors_of_num(lst[69])
    else:
        return 'List must contain at least 70 elements'