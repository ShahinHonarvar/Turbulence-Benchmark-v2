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
    x = numbers[177]
    truncatable_primes = []
    for n in range(11, x):
        if is_prime(n) and all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n))))):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)