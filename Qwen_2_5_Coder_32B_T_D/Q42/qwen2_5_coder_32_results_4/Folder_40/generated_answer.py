def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def factors(n):
        result = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                result.add(i)
                result.add(n // i)
        return result
    n = numbers[7]
    all_factors = factors(n)
    prime_factor_set = {x for x in all_factors if is_prime(x)}
    return prime_factor_set