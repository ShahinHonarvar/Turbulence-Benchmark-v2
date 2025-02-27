def all_left_truncatable_prime(t):
    x = t[14]
    left_truncatable_primes = [2, 3, 5, 7]
    for i in range(10, x):
        is_left_truncatable = True
        for j in range(len(str(i))):
            if int(str(i)[j:]) not in left_truncatable_primes:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)