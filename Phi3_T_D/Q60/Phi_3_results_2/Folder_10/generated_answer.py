def left_right_truncatable_prime(n):

    def is_prime(number):
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def is_truncatable(number):
        if not is_prime(number):
            return False
        str_num = str(number)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                return False
        return True
    return [num for num in range(2, x + 1) if is_truncatable(num)]

def all_left_right_truncatable_prime(nums):
    x = nums[38]
    return left_right_truncatable_prime(x)