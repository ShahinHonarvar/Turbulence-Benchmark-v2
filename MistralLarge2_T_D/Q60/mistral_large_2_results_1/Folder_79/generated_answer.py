def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[91]
    truncatable_primes = []

    def is_truncatable_prime(n):
        left_truncate = right_truncate = str(n)
        while len(left_truncate) > 1:
            left_truncate = left_truncate[1:]
            if not is_prime(int(left_truncate)):
                return False
        while len(right_truncate) > 1:
            right_truncate = right_truncate[:-1]
            if not is_prime(int(right_truncate)):
                return False
        return True
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)