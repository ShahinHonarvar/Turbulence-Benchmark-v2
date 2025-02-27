def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(numbers) > 18:
        num = numbers[18]
        factors = set()
        candidate = 2
        while candidate * candidate <= num:
            if num % candidate == 0 and is_prime(candidate):
                factors.add(candidate)
                while num % candidate == 0:
                    num //= candidate
            candidate += 1
        if num > 1 and is_prime(num):
            factors.add(num)
        return factors
    else:
        return set()