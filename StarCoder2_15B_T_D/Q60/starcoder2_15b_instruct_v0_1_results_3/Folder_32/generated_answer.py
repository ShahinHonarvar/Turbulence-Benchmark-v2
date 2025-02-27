def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[42]
    left_truncatable_primes = []
    right_truncatable_primes = []
    for i in range(2, x + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime and (not str(i).startswith('0')):
            left_truncatable_primes.append(i)
            right_truncatable_primes.append(i)
    for i in range(len(left_truncatable_primes)):
        left_truncatable_primes[i] = int(str(left_truncatable_primes[i])[1:])
    for i in range(len(right_truncatable_primes) - 1, -1, -1):
        right_truncatable_primes[i] = int(str(right_truncatable_primes[i])[:-1])
    left_right_truncatable_primes = []
    for prime in left_truncatable_primes:
        if prime in right_truncatable_primes:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)