def find_primes_between_indices(numbers):
    is_prime = lambda n: all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))
    return sorted((n for i, n in enumerate(numbers) if 23 <= i <= 59 and is_prime(n)), reverse=True)