def prime_factors(numbers):
    if len(numbers) < 22:
        raise IndexError('The list does not have an element at index 21.')

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of_number(n):
        factors = set()
        for i in range(2, n + 1):
            if is_prime(i):
                while n % i == 0:
                    factors.add(i)
                    n //= i
        return factors
    num_to_factor = numbers[21]
    return prime_factors_of_number(num_to_factor)