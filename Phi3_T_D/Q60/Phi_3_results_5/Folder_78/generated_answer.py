def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if not num:
            return False
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not (is_prime(int(str_num[i:])) and is_prime(int(str_num[:i]))):
                return False
        return True
    x = numbers[23]
    result = [p for p in range(2, x + 1) if is_truncatable_prime(p)]
    return result