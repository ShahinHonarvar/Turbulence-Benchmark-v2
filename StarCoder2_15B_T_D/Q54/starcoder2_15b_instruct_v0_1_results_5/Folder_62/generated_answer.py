def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[70]
    result = []
    for i in range(10, x):
        temp = i
        while temp >= 10:
            if not is_prime(temp):
                break
            temp //= 10
        if temp < 10 and is_prime(temp):
            result.append(i)
    return sorted(result)