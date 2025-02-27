def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable(num):
    if num < 10:
        return False
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[758]
    result = []
    for number in range(23, x + 1):
        if is_truncatable(number):
            result.append(number)
    return result