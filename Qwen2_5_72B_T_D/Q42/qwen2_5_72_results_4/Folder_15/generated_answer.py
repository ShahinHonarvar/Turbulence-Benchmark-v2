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
            while n % i == 0 and is_prime(i):
                factor_list.append(i)
                n //= i
        return factor_list
    return set(factors(numbers[10]))