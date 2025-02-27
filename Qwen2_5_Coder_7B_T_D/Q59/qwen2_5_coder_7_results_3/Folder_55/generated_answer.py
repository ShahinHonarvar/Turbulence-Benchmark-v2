def all_left_truncatable_prime(numbers):
    x = numbers[73]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = primes[:]
    for candidate in range(10, x):
        if all((int(candidate[:i + 1]) in primes for i in range(len(candidate)))):
            primes.append(candidate)
            left_truncatable_primes.append(candidate)
    return sorted(left_truncatable_primes, reverse=True)