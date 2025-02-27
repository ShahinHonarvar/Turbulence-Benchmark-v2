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

def all_right_truncatable_prime(numbers):
    x = numbers[78]
    truncatable_primes = []
    for p in range(x - 1, 1, -1):
        if is_prime(p):
            s = str(p)
            if all((is_prime(int(s[:i])) for i in range(1, len(s)))):
                truncatable_primes.append(p)
    return truncatable_primes