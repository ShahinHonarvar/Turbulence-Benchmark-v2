def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        res = set()
        for i in range(2, n + 1):
            while n % i == 0:
                res.add(i)
                n //= i
        return res
    if len(numbers) > 926:
        return factors(numbers[926])
    return set()