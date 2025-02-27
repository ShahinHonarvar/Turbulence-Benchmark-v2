def find_primes_between_indices(lst):
    is_prime = [True] * len(lst)
    for i in range(2, int(len(lst) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, len(lst), i):
                is_prime[j] = False
    primes = [num for idx, num in enumerate(lst) if is_prime[idx] and 16 <= idx <= 25]
    return sorted(primes, reverse=True)