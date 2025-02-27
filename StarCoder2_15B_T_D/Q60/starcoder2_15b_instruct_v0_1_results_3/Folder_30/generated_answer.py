def all_left_right_truncatable_prime(x):

    def is_left_right_truncatable(num):
        num_str = str(num)
        for i in range(len(num_str)):
            truncated_num = int(num_str[i:])
            if not is_prime(truncated_num):
                return False
            truncated_num = int(num_str[:len(num_str) - i])
            if not is_prime(truncated_num):
                return False
        return True

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for num in x:
        if is_left_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)