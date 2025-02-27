def all_left_truncatable_prime(t):
    x = t[20]
    left_truncatable_primes = [2]
    for i in range(3, x):
        is_left_truncatable = True
        for j in range(1, len(str(i))):
            if int(str(i)[j:]) not in left_truncatable_primes:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)