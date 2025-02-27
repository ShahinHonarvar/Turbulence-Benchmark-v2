def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factor_set = set()
    num = numbers[16]
    if num > 1:
        for i in range(2, num + 1):
            while num % i == 0:
                if is_prime(i):
                    factor_set.add(i)
                num //= i
    return factor_set