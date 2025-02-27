def find_primes_between_indices(numbers):
    """Find the sorted list of all prime numbers from index 33 to index 59, both inclusive."""
    primes = []
    for i, num in enumerate(numbers):
        if i < 33 or i > 59:
            continue
        is_prime = True
        for j in range(2, num // 2 + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes