def all_left_right_truncatable_prime(nums):

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

    def is_left_right_truncatable_prime(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if str_num[i] == '0':
                return False
            if not is_prime(int(str_num[i:])):
                return False
            if not is_prime(int(str_num[:len(str_num) - i])):
                return False
        return True
    x = nums[70]
    return sorted([num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)])