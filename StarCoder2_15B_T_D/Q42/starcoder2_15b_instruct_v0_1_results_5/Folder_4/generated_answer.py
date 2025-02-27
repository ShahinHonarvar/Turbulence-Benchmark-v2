def prime_factors(numbers):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors = []
    number = numbers[15]
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            prime_factors.append(i)
    return set(prime_factors)