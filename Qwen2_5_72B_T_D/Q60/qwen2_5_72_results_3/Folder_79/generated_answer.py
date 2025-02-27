def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[91]
    if x < 2:
        return []
    primes = [i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i)]
    truncatable_primes = []
    for prime in primes:
        is_truncatable = all((is_prime(int(str(prime)[:i])) and is_prime(int(str(prime)[i:])) for i in range(1, len(str(prime)))))
        if is_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)