def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    x = x[0]
    result = []
    for i in range(2, x):
        is_truncatable = True
        num = i
        while num > 0:
            if not is_prime(num):
                is_truncatable = False
                break
            num //= 10
        if is_truncatable:
            result.append(i)
    return sorted(result, reverse=True)