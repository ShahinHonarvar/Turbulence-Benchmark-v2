def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def left_and_right_truncatable_prime(n):
    primes = [str(p) for p in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * 2, n + 1, i):
                primes[j] = ''
    return [p for p in primes if p and all((is_prime(int(p[i:])) for i in range(len(p)))) and all((is_prime(int(p[i:len(p) - i])) for i in range(1, len(p) - 1)))]

def all_left_right_truncatable_prime(num_tuple):
    return sorted([p for p in left_and_right_truncatable_prime(num_tuple[57])], reverse=True)