def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[41]
    result = []
    for i in range(1, x):
        num = i
        is_truncatable = True
        while num > 0:
            if not is_prime(num):
                is_truncatable = False
                break
            num //= 10
        if is_truncatable:
            result.append(i)
    result.sort(reverse=True)
    return result