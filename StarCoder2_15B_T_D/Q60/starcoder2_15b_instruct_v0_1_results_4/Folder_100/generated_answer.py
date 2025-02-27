def all_left_right_truncatable_prime(x):
    if x[26] < 1:
        return []
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    truncatable_primes = []
    for prime in primes:
        if prime <= x[26]:
            truncatable_primes.append(prime)
    for i in range(10):
        for j in range(10):
            for prime in primes:
                truncated_prime = int(str(prime)[1:])
                if truncated_prime in primes and truncated_prime <= x[26]:
                    truncatable_primes.append(truncated_prime)
                truncated_prime = int(str(prime)[:-1])
                if truncated_prime in primes and truncated_prime <= x[26]:
                    truncatable_primes.append(truncated_prime)
    truncatable_primes = list(set(truncatable_primes))
    truncatable_primes.sort()
    return truncatable_primes