def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[42]
    result = []
    for i in range(2, x + 1):
        if is_prime(i):
            s = str(i)
            is_truncatable = True
            for j in range(len(s)):
                if not is_prime(int(s[j:])) or not is_prime(int(s[:len(s) - j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(i)
    result.sort()
    return result