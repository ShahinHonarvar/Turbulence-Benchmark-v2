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

def all_left_truncatable_prime(t):
    x = t[36]
    result = []
    for i in range(1, x):
        n = i
        is_left_truncatable = True
        while n > 0:
            if not is_prime(n):
                is_left_truncatable = False
                break
            n //= 10
        if is_left_truncatable:
            result.append(i)
    result.sort(reverse=True)
    return result