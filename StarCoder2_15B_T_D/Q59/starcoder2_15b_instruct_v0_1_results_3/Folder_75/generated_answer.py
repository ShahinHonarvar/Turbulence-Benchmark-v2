def all_left_truncatable_prime(t):
    x = t[41]

    def is_left_truncatable_prime(n):
        if n < 2 or any((digit == 0 for digit in str(n))):
            return False
        for i in range(len(str(n)) - 1):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    return sorted((n for n in range(x) if is_left_truncatable_prime(n)))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True