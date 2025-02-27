def all_left_truncatable_prime(t):
    result = []
    for num in t:
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n >= 10:
        n //= 10
        if not is_prime(n):
            return False
    return True