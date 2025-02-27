from collections import Counter

def prime_factors(int_list):

    def prime_factors_single(n):
        factors = []
        divisor = 2
        while divisor <= n:
            if n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            else:
                divisor += 1
        return factors
    return set(prime_factors_single(int_list[29]))