def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    if len(t) < 26:
        return []
    x = t[25]
    result = []
    for i in range(1, x):
        num = i
        while num < x:
            if not is_prime(num):
                break
            num *= 10
            num += i
        if num == x:
            result.append(i)
    result.sort(reverse=True)
    return result