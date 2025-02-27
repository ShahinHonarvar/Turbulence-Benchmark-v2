def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(numbers) <= 94:
        raise IndexError('List index out of range')
    number = numbers[94]
    factors = set()
    for i in range(2, number + 1):
        while number % i == 0 and is_prime(i):
            factors.add(i)
            number //= i
    return factors