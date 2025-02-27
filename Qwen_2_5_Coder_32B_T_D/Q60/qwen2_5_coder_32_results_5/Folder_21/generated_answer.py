def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[175]
    result = []
    for num in range(10, x + 1):
        s = str(num)
        if '0' in s:
            continue
        all_prime = True
        for i in range(1, len(s) - 1):
            left_truncated = int(s[i:])
            right_truncated = int(s[:-i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                all_prime = False
                break
        if all_prime and is_prime(num):
            result.append(num)
    return result