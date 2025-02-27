def find_primes_between_indices(numbers):
    is_prime = [True] * len(numbers)
    for i in range(2, int(len(numbers) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, len(numbers), i):
                is_prime[j] = False
    primes = [numbers[i] for i in range(187, 272) if is_prime[i] and i >= 187 and (i <= 271)]
    primes.sort()
    return primes