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

def all_right_truncatable_primes(numbers):
    x = numbers[7]
    truncatable_primes = []
    for p in range(2, x):
        if not is_prime(p):
            continue
        original_p = p
        while p > 0:
            if not is_prime(p):
                break
            p = p // 10
        if p != 0:
            truncatable_primes.append(original_p)
    return sorted(truncatable_primes)