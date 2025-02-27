def prime_factors(numbers):
    number = numbers[990]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors = []
    for i in range(2, number + 1):
        if is_prime(i) and number % i == 0:
            prime_factors.append(i)
    return set(prime_factors)