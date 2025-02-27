def all_left_right_truncatable_prime(x):
    x = x[0]
    left_truncatable_primes = []
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    for i in range(x, 1, -1):
        if is_prime(i):
            left_truncatable_primes.append(i)
    for i in range(x):
        if is_prime(i):
            right_truncatable_primes.append(i)
    result = [p for p in left_truncatable_primes if p in right_truncatable_primes]
    result.sort(reverse=True)
    return result