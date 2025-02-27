def all_right_truncatable_prime(primes):
    x = primes[767]
    right_truncatables = []
    for p in reversed(primes):
        if all((is_prime(int(p[:len(p) - i])) for i in range(len(p)))):
            if int(p[:len(p) - 1]) != 0:
                right_truncatables.append(p)
    right_truncatables = list(filter(lambda p: int(p) < x, right_truncatables))
    return sorted(right_truncatables, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True