def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        str_num = str(num)
        while len(str_num) > 1:
            if not is_prime(int(str_num)) or not is_prime(int(str_num[::-1])):
                return False
            str_num = str_num[1:-1]
        return True if is_prime(int(str_num)) else False
    x = nums[24]
    result = [num for num in range(11, x + 1) if '0' not in str(num) and is_truncatable_prime(num)]
    return sorted(result)