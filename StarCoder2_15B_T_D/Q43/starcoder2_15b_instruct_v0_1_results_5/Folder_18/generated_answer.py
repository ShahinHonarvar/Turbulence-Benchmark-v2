def find_primes_between_indices(numbers):
    is_prime = [False, False] + [True] * (max(numbers) - 1)
    for i in range(2, int(max(numbers) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max(numbers) + 1, i):
                is_prime[j] = False
    primes = [i for i in numbers[430:806] if is_prime[i]]
    primes.sort()
    return primes