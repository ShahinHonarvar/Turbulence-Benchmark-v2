def all_left_truncatable_prime(tup):
    x = tup[65]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable = True
        for j in range(len(str(i)) - 1):
            if int(str(i)[j + 1:]) % i != 0:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes