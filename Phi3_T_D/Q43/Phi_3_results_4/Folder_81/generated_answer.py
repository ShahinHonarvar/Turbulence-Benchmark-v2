def find_primes_between_indices(lst):
    primes = []
    for n in lst[59:98]:
        if n < 2:
            continue
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            primes.append(n)
    return sorted(primes, reverse=True)