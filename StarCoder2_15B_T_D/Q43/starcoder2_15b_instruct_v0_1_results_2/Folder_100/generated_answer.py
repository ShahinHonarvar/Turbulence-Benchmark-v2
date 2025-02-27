def find_primes_between_indices(lst):
    primes = []
    for n in lst[25:63]:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return sorted(primes)