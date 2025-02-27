def prime_factors(num_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors_number(n):
        factors = set()
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
            if divisor * divisor > n:
                if n > 1:
                    factors.add(n)
                break
        return factors
    if 47 < len(num_list):
        n = num_list[47]
        return prime_factors_number(n)
    else:
        raise IndexError('Index out of range.')