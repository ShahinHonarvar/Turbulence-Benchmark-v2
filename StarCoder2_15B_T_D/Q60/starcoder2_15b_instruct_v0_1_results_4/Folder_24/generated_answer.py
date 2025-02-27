def is_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(len(str_num)):
        truncated_num = int(str_num[i:])
        if not is_prime(truncated_num):
            return False
    for i in range(len(str_num) - 1, 0, -1):
        truncated_num = int(str_num[:i])
        if not is_prime(truncated_num):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[65]
    return sorted([num for num in range(2, x + 1) if is_truncatable_prime(num)], reverse=True)