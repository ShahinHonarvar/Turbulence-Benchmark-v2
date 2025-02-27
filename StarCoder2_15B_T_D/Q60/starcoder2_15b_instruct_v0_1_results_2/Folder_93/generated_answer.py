def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str) - 1):
            truncated_num = int(num_str[i + 1:])
            if not is_prime(truncated_num):
                return False
            truncated_num = int(num_str[:-i - 1])
            if not is_prime(truncated_num):
                return False
        return True

    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = nums[11]
    return sorted([num for num in range(2, x + 1) if is_truncatable_prime(num)])