def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[36]
    result = []
    for i in range(2, x):
        if is_prime(i):
            is_left_truncatable = True
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    is_left_truncatable = False
                    break
                temp //= 10
            if is_left_truncatable:
                result.append(i)
    result.sort()
    return result