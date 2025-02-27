def find_primes_between_indices(numbers):
    primes = [n for n in numbers[35:41] if n > 1 and all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))]
    return sorted(primes, reverse=True)