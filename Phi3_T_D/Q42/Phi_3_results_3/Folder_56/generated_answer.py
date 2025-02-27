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

def prime_factors(numbers):
    if len(numbers) < 61:
        raise IndexError('List must contain at least 61 elements')

    def factors(n):
        result = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                result.add(i)
                n = n // i
        if n > 1 and is_prime(n):
            result.add(n)
        return result
    return factors(numbers[60])