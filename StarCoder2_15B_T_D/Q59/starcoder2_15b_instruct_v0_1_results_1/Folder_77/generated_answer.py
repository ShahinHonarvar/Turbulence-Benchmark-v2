import math

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime

def all_left_truncatable_prime(tup):
    x = tup[0]
    n = 10 ** (len(str(x)) - 1)
    prime = sieve_of_eratosthenes(n)
    left_truncatable = []
    for i in range(n, x):
        if prime[i]:
            is_left_truncatable = True
            for j in range(len(str(i)) - 1):
                if not prime[int(str(i)[j + 1:])]:
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable.append(i)
    return sorted(left_truncatable, reverse=True)