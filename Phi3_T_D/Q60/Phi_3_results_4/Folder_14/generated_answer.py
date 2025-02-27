def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_and_right_truncatable(num):
    if num < 10:
        return False
    if not is_prime(num):
        return False
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[78]
    result = [p for p in range(x, 0, -1) if is_left_and_right_truncatable(p)]
    return result