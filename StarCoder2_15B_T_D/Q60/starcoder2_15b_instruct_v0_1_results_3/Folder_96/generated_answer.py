def all_left_right_truncatable_prime(t):
    x = t[29]
    truncatable_primes = []
    for prime in range(2, x + 1):
        is_truncatable = True
        for digit in range(1, len(str(prime))):
            left_truncation = int(str(prime)[digit:])
            right_truncation = int(str(prime)[:len(str(prime)) - digit])
            if not (is_prime(left_truncation) and is_prime(right_truncation)):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True