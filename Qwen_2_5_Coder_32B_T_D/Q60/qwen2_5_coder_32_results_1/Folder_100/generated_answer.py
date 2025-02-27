def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str) - 1):
            if not (is_prime(int(num_str[i:])) and is_prime(int(num_str[:-i]))):
                return False
        return is_prime(num) and is_prime(int(num_str[1:])) and is_prime(int(num_str[:-1]))
    x = numbers[26]
    result = [n for n in range(10, x + 1) if is_lr_truncatable_prime(n)]
    return result