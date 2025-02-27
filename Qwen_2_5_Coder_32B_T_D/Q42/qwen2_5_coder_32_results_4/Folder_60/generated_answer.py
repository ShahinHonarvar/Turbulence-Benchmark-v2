def prime_factors(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def factors(num):
        result = set()
        for i in range(2, num + 1):
            while num % i == 0:
                result.add(i)
                num //= i
        return result
    if len(numbers) <= 88:
        return set()
    num = numbers[88]
    return factors(num) if is_prime(num) else factors(num)