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

def all_left_right_truncatable_prime(t):
    x = t[0]
    result = []
    for i in range(10, x + 1):
        s = str(i)
        if not is_prime(i):
            continue
        for j in range(1, len(s)):
            if not is_prime(int(s[j:])) or not is_prime(int(s[:-j])):
                break
        else:
            result.append(i)
    return sorted(result)