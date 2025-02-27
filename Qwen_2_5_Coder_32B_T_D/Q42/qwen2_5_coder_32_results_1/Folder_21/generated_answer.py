def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def factors(n):
        result = set()
        for i in range(2, n + 1):
            while n % i == 0:
                result.add(i)
                n //= i
        return result
    if len(numbers) < 411:
        return set()
    return factors(numbers[410])