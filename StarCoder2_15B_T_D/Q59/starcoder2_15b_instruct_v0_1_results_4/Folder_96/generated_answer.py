def all_left_truncatable_prime(input_tuple):
    x = input_tuple[29]
    primes = [True for i in range(x)]
    primes[0] = False
    primes[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, x, i):
                primes[j] = False
    left_truncatable_primes = []
    for i in range(x):
        if primes[i]:
            is_left_truncatable = True
            temp = i
            while temp > 0:
                if not primes[temp]:
                    is_left_truncatable = False
                    break
                temp //= 10
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)