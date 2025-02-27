def all_left_truncatable_prime(numbers):
    primes = [2, 3, 5, 7]
    for i in range(10, numbers[41]):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    left_truncatable_primes = []
    for prime in reversed(primes):
        str_prime = str(prime)
        for i in range(len(str_prime)):
            truncated = int(str_prime[i:])
            if truncated not in primes:
                break
        else:
            left_truncatable_primes.append(prime)
    return left_truncatable_primes