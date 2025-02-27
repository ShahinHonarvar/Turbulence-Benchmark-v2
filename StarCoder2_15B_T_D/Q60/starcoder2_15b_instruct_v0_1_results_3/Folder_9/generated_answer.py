def all_left_right_truncatable_prime(x):
    x = x[29]
    is_prime = lambda n: all((n % i for i in range(2, int(n ** 0.5) + 1)))
    truncatable_primes = []
    for i in range(10, x + 1):
        if is_prime(i):
            is_truncatable = True
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])) or not is_prime(int(str(i)[:-j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)