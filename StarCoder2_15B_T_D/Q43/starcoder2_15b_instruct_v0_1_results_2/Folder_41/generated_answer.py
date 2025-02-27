def find_primes_between_indices(numbers):
    is_prime = [True] * len(numbers)
    for i in range(2, int(len(numbers) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, len(numbers), i):
                is_prime[j] = False
    primes = [num for idx, num in enumerate(numbers) if is_prime[idx] and 45 <= idx <= 80]
    return sorted(primes, reverse=True)