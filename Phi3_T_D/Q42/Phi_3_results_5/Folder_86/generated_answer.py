def prime_factors(int_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n > 1:
            if n % divisor == 0 and is_prime(divisor):
                factors.add(divisor)
                n = n // divisor
            else:
                divisor += 1
        return factors
    if 194 < len(int_list):
        return None
    return get_prime_factors(int_list[194])