def all_left_right_truncatable_prime(t):
    x = t[36]

    def is_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num) - 1):
            truncated_num = int(str_num[i + 1:])
            if not is_prime(truncated_num):
                return False
            truncated_num = int(str_num[:-i - 1])
            if not is_prime(truncated_num):
                return False
        return True

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result)