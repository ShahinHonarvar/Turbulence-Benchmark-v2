def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factor_list = []
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                factor_list.append(i)
        return factor_list
    target_number = numbers[993]
    prime_factors_set = set(factors(target_number))
    return prime_factors_set