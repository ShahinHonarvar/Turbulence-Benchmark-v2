def all_left_truncatable_prime(numbers):
    x = numbers[52]
    left_truncatable_primes = []
    for prime in range(2, x):
        is_left_truncatable = True
        temp = prime
        while temp > 0:
            if temp % 10 == 0:
                is_left_truncatable = False
                break
            temp //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes