def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[67]
    result = []
    for i in range(2, x):
        is_truncatable = True
        temp = i
        while temp > 0:
            if not is_prime(temp):
                is_truncatable = False
                break
            temp //= 10
        if is_truncatable:
            result.append(i)
    return sorted(result, reverse=True)