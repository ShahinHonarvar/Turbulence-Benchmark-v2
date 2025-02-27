def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[87]
    result = []
    for num in range(2, x):
        str_num = str(num)
        if '0' not in str_num:
            truncatable = True
            for i in range(len(str_num)):
                if not is_prime(int(str_num[i:])):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    return result