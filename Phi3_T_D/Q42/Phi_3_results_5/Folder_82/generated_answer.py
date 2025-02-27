def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = numbers[83]
    factors_set = set()
    if num == 1:
        return factors_set
    for i in range(2, num + 1):
        while num % i == 0 and is_prime(i):
            factors_set.add(i)
            num //= i
    return factors_set