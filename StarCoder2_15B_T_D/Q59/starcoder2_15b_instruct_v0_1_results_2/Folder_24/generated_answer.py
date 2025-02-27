def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[65]
    result = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j < x:
                if not is_prime(j):
                    break
                j //= 10
            else:
                result.append(i)
    result.sort(reverse=True)
    return result