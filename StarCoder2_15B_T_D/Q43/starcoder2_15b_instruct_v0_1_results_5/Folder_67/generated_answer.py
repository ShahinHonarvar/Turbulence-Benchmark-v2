def find_primes_between_indices(numbers):
    is_prime = [True] * len(numbers)
    for i in range(2, int(len(numbers) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, len(numbers), i):
                is_prime[j] = False
    primes = []
    for i in range(17, 80):
        if is_prime[i] and numbers[i] > 1:
            primes.append(numbers[i])
    return sorted(primes, reverse=True)