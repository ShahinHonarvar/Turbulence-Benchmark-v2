def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[30]
    primes = [str(i) for i in range(2, x) if all((i % d for d in range(2, int(i ** 0.5) + 1)))]
    left_truncatable = []
    for prime in primes:
        is_truncatable = True
        for i in range(len(prime)):
            truncated = prime[i:]
            if int(truncated) < 2 or not int(truncated) in primes:
                is_truncatable = False
                break
        if is_truncatable:
            left_truncatable.append(int(prime))
    return left_truncatable