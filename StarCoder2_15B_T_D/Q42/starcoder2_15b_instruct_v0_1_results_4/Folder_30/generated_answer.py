def prime_factors(numbers):

    def is_prime(n):
        return all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))
    prime_factors = []
    number_at_94 = numbers[94]
    for i in range(2, number_at_94 + 1):
        if is_prime(i) and number_at_94 % i == 0:
            prime_factors.append(i)
    return set(prime_factors)