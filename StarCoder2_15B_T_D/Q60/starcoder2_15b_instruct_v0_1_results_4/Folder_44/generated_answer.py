def all_left_right_truncatable_prime(numbers):
    x = numbers[39]
    left_truncatable_primes = [2, 3, 5, 7]
    right_truncatable_primes = [2, 3, 5, 7]
    for i in range(10):
        left_truncatable_primes = [p * 10 + i for p in left_truncatable_primes for i in range(10) if is_prime(p * 10 + i)]
        right_truncatable_primes = [i * 10 + d for i in range(1, 10) for d in right_truncatable_primes if is_prime(i * 10 + d)]
    left_right_truncatable_primes = [p for p in left_truncatable_primes if p <= x and p in right_truncatable_primes]
    return sorted(left_right_truncatable_primes)