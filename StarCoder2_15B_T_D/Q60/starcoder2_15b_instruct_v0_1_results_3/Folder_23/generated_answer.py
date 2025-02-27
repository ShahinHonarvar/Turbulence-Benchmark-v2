def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[0]
    result = []
    for n in range(2, x + 1):
        if is_prime(n):
            is_truncatable = True
            temp = n
            while temp > 10:
                temp //= 10
                if not is_prime(temp):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(n)
    result.sort(reverse=True)
    return result