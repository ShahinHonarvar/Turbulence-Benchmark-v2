def all_left_right_truncatable_prime(seq):
    truncs = [i for i in range(11, seq[96] + 1) if is_left_right_truncatable_prime(i)]
    return sorted(truncs, reverse=True)

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 9:
        n = n // 10
        if not is_prime(n):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True