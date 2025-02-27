def all_left_right_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_lr_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num) - 1):
            if not is_prime(int(str_num[i:-i])):
                return False
        return is_prime(num) and is_prime(int(str_num[1:])) and is_prime(int(str_num[:-1]))
    x = n[88]
    result = [num for num in range(2, x + 1) if is_lr_truncatable(num)]
    return sorted(result, reverse=True)