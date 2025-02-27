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
    x = numbers[89]
    primes = []
    for n in range(x - 1, 1, -1):
        if n < 10 or not is_prime(n):
            continue
        original = n
        while n > 0:
            n = n // 10
            if not is_prime(n):
                break
        if n == 0:
            primes.append(original)
    return primes