def find_primes_between_indices(numbers):
    sublist = numbers[80:85]
    primes = [n for n in sublist if all((n % i != 0 for i in range(2, n)))]
    return sorted(primes, reverse=True)