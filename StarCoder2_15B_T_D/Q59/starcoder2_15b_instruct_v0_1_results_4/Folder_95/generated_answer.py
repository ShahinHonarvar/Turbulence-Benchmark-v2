def all_left_truncatable_prime(tup):
    x = tup[77]
    left_truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort()
    return left_truncatable_primes