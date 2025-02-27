def all_right_truncatable_prime(t):
    x = t[20]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = []
    for prime in primes:
        right_truncatable = True
        temp = prime
        while temp > 9:
            temp //= 10
            if not is_prime(temp):
                right_truncatable = False
                break
        if right_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True