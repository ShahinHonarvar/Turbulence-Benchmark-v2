def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    str_num = str(num)
    if '0' in str_num:
        return False
    while len(str_num) > 1:
        str_num = str_num[1:-1]
        if not str_num or not is_prime(int(str_num)):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[7]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)