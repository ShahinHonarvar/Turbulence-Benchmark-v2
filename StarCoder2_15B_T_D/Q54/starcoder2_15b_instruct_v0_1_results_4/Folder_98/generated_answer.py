def all_right_truncatable_prime(numbers: tuple) -> list:
    x = numbers[8]
    right_truncatable_primes = []
    primes = [True] * x
    for i in range(2, int(x ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, x, i):
                primes[j] = False
    for i in range(2, x):
        if primes[i]:
            temp = i
            while temp > 9:
                temp //= 10
                if not primes[temp]:
                    break
            else:
                right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes