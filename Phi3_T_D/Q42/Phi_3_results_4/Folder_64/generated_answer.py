def prime_factors(integers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_number(num):
        factors = set()
        if is_prime(num):
            factors.add(num)
        divisor = 2
        while divisor <= num:
            if num % divisor == 0 and is_prime(divisor):
                factors.add(divisor)
                num //= divisor
            else:
                divisor += 1
        return factors
    return prime_factors_number(integers[1])