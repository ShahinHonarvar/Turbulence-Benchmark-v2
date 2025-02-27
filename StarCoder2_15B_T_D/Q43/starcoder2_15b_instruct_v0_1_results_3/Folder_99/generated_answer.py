def find_primes_between_indices(numbers):
    max_number = max(numbers)
    is_prime = [True] * (max_number + 1)
    for i in range(2, int(max_number ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_number + 1, i):
                is_prime[j] = False
    primes = []
    for i in range(187, 272):
        if is_prime[numbers[i]]:
            primes.append(numbers[i])
    primes.sort()
    return primes