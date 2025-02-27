def all_left_truncatable_prime(t):
    x = t[54]
    return sorted([p for p in range(2, x) if is_left_truncatable_prime(p)])

def is_left_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_left_truncatable_prime(int(str(n)[1:]))

def is_prime(n):
    return all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))