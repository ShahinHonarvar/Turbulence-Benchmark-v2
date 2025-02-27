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
    x = numbers[433]
    primes = [2, 3, 5, 7]
    candidates = [2, 3, 5, 7]
    while candidates:
        candidate = candidates.pop()
        if candidate < x:
            primes.append(candidate)
            for digit in ['1', '3', '7', '9']:
                candidates.append(int(str(candidate) + digit))
    right_truncatable_primes = [p for p in primes if all((is_prime(int(str(p)[:i])) for i in range(1, len(str(p)) + 1)))]
    return sorted(right_truncatable_primes, reverse=True)