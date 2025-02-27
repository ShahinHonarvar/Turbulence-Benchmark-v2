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
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                result.add(i)
                if is_prime(i):
                    result.add(i)
                if is_prime(n // i):
                    result.add(n // i)
                result.update(factors(i))
                result.update(factors(n // i))
        if is_prime(n):
            result.add(n)
        return result
    if len(numbers) > 247:
        return factors(numbers[247])
    else:
        return set()