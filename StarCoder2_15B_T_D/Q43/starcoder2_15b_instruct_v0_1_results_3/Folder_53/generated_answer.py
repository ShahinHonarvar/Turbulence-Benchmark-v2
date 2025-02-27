def find_primes_between_indices(lst):
    if len(lst) < 59:
        return []
    primes = []
    for i in range(43, 60):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    primes.sort(reverse=True)
    return primes