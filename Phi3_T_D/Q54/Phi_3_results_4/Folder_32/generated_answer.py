def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    if num < 10:
        return False
    str_num = str(num)
    while str_num != '':
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[:-1]
    return True

def all_right_truncatable_prime(tup):
    x = tup[42]
    return sorted([num for num in range(2, x) if is_right_truncatable_prime(num)])