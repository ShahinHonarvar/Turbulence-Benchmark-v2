def find_primes_between_indices(numbers):
    is_prime = lambda n: all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))
    primes = [n for n in numbers[5:9] if is_prime(n)]
    return sorted(primes, reverse=True)