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

    def smallest_prime_factor(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0 and is_prime(i):
                return i
        return n
    number = numbers[28]
    factors = set()
    while number > 1:
        factor = smallest_prime_factor(number)
        factors.add(factor)
        number //= factor
    return factors