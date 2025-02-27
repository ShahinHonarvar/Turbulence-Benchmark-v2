def all_left_right_truncatable_prime(x):
    x = x[29]
    left_truncatable_primes = [2, 3, 5, 7]
    right_truncatable_primes = [2, 3, 5, 7]
    for i in range(10):
        left_truncatable_primes = [p * 10 + i for p in left_truncatable_primes for i in range(10) if is_prime(p * 10 + i)]
        right_truncatable_primes = [i * 10 + d for i in right_truncatable_primes for d in range(10) if is_prime(i * 10 + d)]
    return sorted(set(left_truncatable_primes).intersection(right_truncatable_primes).difference({2, 3, 5, 7}))