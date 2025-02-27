def find_primes_between_indices(numbers):
    start, end = (25, 72)
    primes = []
    for i in range(start, end + 1):
        if all((numbers[i] % x != 0 for x in range(2, int(numbers[i] ** 0.5) + 1))):
            primes.append(numbers[i])
    return sorted(primes)