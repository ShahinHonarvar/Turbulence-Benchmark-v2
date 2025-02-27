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
    x = numbers[94]

    def is_left_right_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        while len(str_num) > 1:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:-1]
        return is_prime(int(str_num))
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable(n)])