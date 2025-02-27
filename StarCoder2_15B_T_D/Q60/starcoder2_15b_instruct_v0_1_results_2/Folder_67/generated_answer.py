def all_left_right_truncatable_prime(x):
    primes = [True] * (x + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, x + 1, i):
                primes[j] = False
    primes = [i for i in range(x + 1) if primes[i]]
    primes = [p for p in primes if '0' not in str(p)]
    left_right_truncatable_primes = []
    for p in primes:
        is_left_right_truncatable = True
        temp = p
        while temp >= 10:
            temp = int(str(temp)[1:])
            if temp not in primes:
                is_left_right_truncatable = False
                break
        temp = p
        while temp >= 10:
            temp = int(str(temp)[:-1])
            if temp not in primes:
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(p)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes