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

def all_left_truncatable_prime(numbers):
    x = numbers[52]
    primes = [str(p) for p in range(2, x) if is_prime(p)]
    left_truncatable_primes = []
    for p in primes:
        if all((is_prime(int(p[i:])) for i in range(len(p)))):
            left_truncatable_primes.append(int(p))
    return sorted(left_truncatable_primes, reverse=True)