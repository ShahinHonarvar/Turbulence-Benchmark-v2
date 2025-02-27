def is_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:len(str_num) - i])):
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
    result = []
    for num in tup:
        if is_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result