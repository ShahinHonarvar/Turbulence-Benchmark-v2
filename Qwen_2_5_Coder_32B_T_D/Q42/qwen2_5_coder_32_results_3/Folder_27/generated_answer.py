def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        result = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                result.add(i)
                result.add(n // i)
        return result
    if len(numbers) > 56:
        num = numbers[56]
        return {f for f in factors(num) if is_prime(f)}
    else:
        return set()