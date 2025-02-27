def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num) - 1):
            if not is_prime(int(str_num[:i])) or not is_prime(int(str_num[i:])):
                return False
        return is_prime(num) and is_prime(int(str_num[1:])) and is_prime(int(str_num[:-1]))
    x = numbers[11]
    result = [num for num in range(10, x + 1) if is_truncatable_prime(num)]
    return result