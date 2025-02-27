def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[57]
    primes = [str(i) for i in range(2, x) if is_prime(i)]
    left_truncatables = []
    for prime in primes:
        is_truncatable = True
        for i in range(len(prime)):
            if not is_prime(int(prime[i:])):
                is_truncatable = False
                break
        if is_truncatable:
            left_truncatables.append(int(prime))
    return sorted(left_truncatables, reverse=True)