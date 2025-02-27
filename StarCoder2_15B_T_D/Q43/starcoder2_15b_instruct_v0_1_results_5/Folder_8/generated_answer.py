def find_primes_between_indices(numbers):
    primes = []
    for i, n in enumerate(numbers):
        if i < 43 or i > 76:
            continue
        is_prime = True
        for j in range(2, n):
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    primes.sort(reverse=True)
    return primes