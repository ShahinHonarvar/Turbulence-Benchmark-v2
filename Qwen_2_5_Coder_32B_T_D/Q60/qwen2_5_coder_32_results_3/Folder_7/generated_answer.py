def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[803]
    result = []
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        left_right_test = True
        for i in range(len(str_num) - 1):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:len(str_num) - i])):
                left_right_test = False
                break
        if left_right_test and is_prime(num):
            result.append(num)
    return result