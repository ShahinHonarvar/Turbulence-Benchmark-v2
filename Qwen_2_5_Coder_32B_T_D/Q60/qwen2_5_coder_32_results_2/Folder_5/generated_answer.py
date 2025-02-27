def all_left_right_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(num):
        str_num = str(num)
        for i in range(1, len(str_num) - 1):
            if '0' in str_num[i:]:
                return False
            if not is_prime(int(str_num[i:])):
                return False
            if not is_prime(int(str_num[:-i])):
                return False
        return is_prime(int(str_num[-1])) and is_prime(int(str_num[0]))
    x = n[55]
    result = [num for num in range(2, x + 1) if is_lr_truncatable_prime(num)]
    return result