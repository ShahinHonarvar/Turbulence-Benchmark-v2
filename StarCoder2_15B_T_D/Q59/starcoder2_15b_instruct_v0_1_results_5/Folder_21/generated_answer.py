def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[175]
    result = []
    for i in range(2, x):
        if is_prime(i):
            is_left_truncatable = True
            for j in range(len(str(i)) - 1):
                if not is_prime(int(str(i)[j + 1:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                result.append(i)
    return sorted(result)