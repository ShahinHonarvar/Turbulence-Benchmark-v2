def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors_of(num):
        factors = set()
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                factors.add(i)
        return factors
    if 97 < len(numbers):
        num = numbers[97]
        return prime_factors_of(num)
    else:
        raise IndexError('Index out of range. No element at index 97.')