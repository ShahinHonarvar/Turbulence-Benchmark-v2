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

def is_right_truncatable_prime(n, primes):
    for i in range(1, 10):
        if not is_prime(int(str(n)[:-1])):
            return False
        n = int(str(n)[:-1])
        if n == 0:
            return True
    return n == 0

def all_right_truncatable_prime(numbers):
    x = numbers[803] if 803 < len(numbers) else 0
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted((p for p in primes if is_right_truncatable_prime(p, primes)))