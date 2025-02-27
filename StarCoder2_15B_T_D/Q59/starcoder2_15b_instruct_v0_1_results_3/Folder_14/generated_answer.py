def is_prime(n):
    return all((n % i for i in range(2, int(n ** 0.5) + 1)))

def all_left_truncatable_prime(t):
    x = t[78]
    return sorted(filter(is_prime, range(2, x)), reverse=True)