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
    x = numbers[41]
    result = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            valid = True
            left_str = str_num
            right_str = str_num
            while len(left_str) > 1:
                left_str = left_str[1:]
                right_str = right_str[:-1]
                if not is_prime(int(left_str)) or not is_prime(int(right_str)):
                    valid = False
                    break
            if valid and is_prime(num):
                result.append(num)
    return sorted(result, reverse=True)