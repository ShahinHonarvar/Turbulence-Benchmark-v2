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
    x = numbers[433]
    primes = []
    for n in range(2, x):
        s = str(n)
        if '0' in s:
            continue
        if all((is_prime(int(s[i:])) for i in range(len(s)))):
            primes.append(n)
    return sorted(primes, reverse=True)