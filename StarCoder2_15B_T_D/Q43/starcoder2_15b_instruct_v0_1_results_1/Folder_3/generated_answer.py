def find_primes_between_indices(numbers):
    max_prime = max(numbers)
    is_prime = [True] * (max_prime + 1)
    for i in range(2, int(max_prime ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_prime + 1, i):
                is_prime[j] = False
    primes = [p for p in numbers if is_prime[p]]
    primes.sort(reverse=True)
    return primes[80:85]