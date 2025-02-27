def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = set()
    for i in range(2, numbers[3] + 1):
        if numbers[3] % i == 0 and is_prime(i):
            result.add(i)
    return result