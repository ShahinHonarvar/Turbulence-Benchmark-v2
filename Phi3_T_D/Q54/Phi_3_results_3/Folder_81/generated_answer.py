def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, original=True):
    if is_prime(n):
        if original:
            for d in str(n):
                if not is_prime(int(d)):
                    return False
        return n > 0 and all((is_right_truncatable_prime(n // 10, False) for _ in range(len(str(n)))))
    return False

def all_right_truncatable_prime(t):
    return sorted([p for p in range(t[98]) if is_right_truncatable_prime(p)])