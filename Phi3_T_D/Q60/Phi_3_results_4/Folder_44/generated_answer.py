def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_left_right(n):
    s_n = str(n)
    for i in range(1, len(s_n)):
        if not (is_prime(int(s_n[i:])) and is_prime(int(s_n[:i]))):
            return False
    return True

def all_left_right_truncatable_prime(integers):
    x = integers[39]
    return sorted([p for p in range(2, x + 1) if is_prime(p) and is_truncatable_left_right(p)])