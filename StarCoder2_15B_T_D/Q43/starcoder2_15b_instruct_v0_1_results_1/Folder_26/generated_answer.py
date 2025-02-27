def find_primes_between_indices(numbers):
    """Find the sorted list of all prime numbers from index 23 to index 48, both inclusive."""
    sublist = numbers[23:50]
    primes = []
    for num in sublist:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes)