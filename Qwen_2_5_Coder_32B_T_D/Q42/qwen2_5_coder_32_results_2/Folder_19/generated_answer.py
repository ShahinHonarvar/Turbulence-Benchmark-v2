def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def factors(num):
        result = set()
        for i in range(2, num + 1):
            while num % i == 0:
                if is_prime(i):
                    result.add(i)
                num //= i
        return result
    if len(numbers) < 14:
        return set()
    return factors(numbers[13])