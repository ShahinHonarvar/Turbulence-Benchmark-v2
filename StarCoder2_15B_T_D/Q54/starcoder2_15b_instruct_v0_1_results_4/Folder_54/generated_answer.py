def all_right_truncatable_prime(t):
    x = t[88]
    right_truncatable_primes = []
    for i in range(1, x):
        is_right_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            if int(str(i)[j + 1:]) % i != 0:
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)