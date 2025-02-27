def all_right_truncatable_prime(numbers):
    x = numbers[803]
    right_truncatable_primes = []
    for prime in primes_less_than(x):
        is_right_truncatable = True
        while prime >= 10:
            prime //= 10
            if not is_prime(prime):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    right_truncatable_primes.sort()
    return right_truncatable_primes