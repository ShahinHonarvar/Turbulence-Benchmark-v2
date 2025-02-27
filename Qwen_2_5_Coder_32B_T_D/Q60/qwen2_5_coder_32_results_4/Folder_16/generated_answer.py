def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[792]
    result = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        valid = True
        for i in range(1, len(str_num) - 1):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                valid = False
                break
        if valid and is_prime(int(str_num[0])) and is_prime(int(str_num[-1])):
            result.append(num)
    return result