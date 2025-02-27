def find_primes_between_indices(lst):
    prime_numbers = []
    for i in range(33, 60):
        if all((lst[i] % n != 0 for n in range(2, int(lst[i] ** 0.5) + 1))):
            prime_numbers.append(lst[i])
    return sorted(prime_numbers, reverse=True)