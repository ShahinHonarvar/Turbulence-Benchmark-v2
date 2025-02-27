def find_primes_between_indices(numbers):
    """
    Finds the sorted list of all prime numbers from index 20 to index 25, both inclusive, in a list of integers.
    The returned list is in descending order. If no prime number exists in the specified range, an empty list is returned.
    """
    is_prime = [True] * len(numbers)
    for i in range(2, int(len(numbers) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, len(numbers), i):
                is_prime[j] = False
    primes = [number for i, number in enumerate(numbers) if is_prime[i] and 20 <= i <= 25]
    primes.sort(reverse=True)
    return primes