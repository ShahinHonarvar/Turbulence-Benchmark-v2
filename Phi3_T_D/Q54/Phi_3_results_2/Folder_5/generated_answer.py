def all_right_truncatable_prime(t):
    primes = [2, 3, 5, 7]
    truncated = set((str(p) for p in primes))
    lim = x = t[55]
    for num in range(11, x, 2):
        if all((num % p for p in primes)) and str(num)[-1] in truncated:
            truncated.add(str(num))
            primes.append(num)
    return sorted([int(p[:-1]) for p in truncated])