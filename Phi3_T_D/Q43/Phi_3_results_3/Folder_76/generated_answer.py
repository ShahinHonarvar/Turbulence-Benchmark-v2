def find_primes_between_indices(numbers):
    start, end = (149, 979)
    primes = []
    for i in range(start, end + 1):
        if all((i % n > 0 for n in range(2, int(i ** 0.5) + 1))):
            primes.append(numbers[i])
    return sorted(primes)