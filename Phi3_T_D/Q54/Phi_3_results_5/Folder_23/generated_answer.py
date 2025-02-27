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
    x = numbers[77]
    primes = [str(p) for p in range(x) if is_prime(p)]
    truncatables = []
    for prime in primes:
        is_truncatable = True
        for i in range(1, len(prime)):
            if not is_prime(int(prime[:len(prime) - i])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatables.append(int(prime))
    return sorted(truncatables, reverse=True)