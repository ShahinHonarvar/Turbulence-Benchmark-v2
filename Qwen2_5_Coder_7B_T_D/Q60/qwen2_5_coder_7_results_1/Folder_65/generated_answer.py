def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[32]
    result = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if is_prime(num):
            left_truncatable = True
            right_truncatable = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    left_truncatable = False
                if not is_prime(int(str_num[:-i])):
                    right_truncatable = False
            if left_truncatable and right_truncatable:
                result.append(num)
    return sorted(result)