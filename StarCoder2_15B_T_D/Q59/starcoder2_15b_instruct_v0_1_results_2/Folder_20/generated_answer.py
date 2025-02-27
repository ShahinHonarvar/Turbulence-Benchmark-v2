def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[100]
    primes = [True] * x
    primes[0] = False
    primes[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, x, i):
                primes[j] = False
    left_truncatable_primes = []
    for i in range(2, x):
        if primes[i]:
            number = i
            is_left_truncatable = True
            while number > 9:
                number //= 10
                if not primes[number]:
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)