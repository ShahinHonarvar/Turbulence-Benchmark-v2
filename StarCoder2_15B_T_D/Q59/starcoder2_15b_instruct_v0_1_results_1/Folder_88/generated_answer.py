def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    result = []
    for n in range(2, x):
        if is_prime(n):
            is_left_truncatable = True
            while n > 0:
                if not is_prime(n) or n % 10 == 0:
                    is_left_truncatable = False
                    break
                n //= 10
            if is_left_truncatable:
                result.append(n)
    result.sort()
    return result