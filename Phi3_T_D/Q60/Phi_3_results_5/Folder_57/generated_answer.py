def all_left_right_truncatable_prime(input_range):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(number):
        str_num = str(number)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                return False
        return True
    x = input_range[54]
    return sorted((num for num in range(2, x + 1) if is_truncatable_prime(num)), reverse=True)