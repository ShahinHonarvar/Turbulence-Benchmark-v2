def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        length = len(str_n)
        for i in range(length):
            truncated = int(str_n[i:length] + str_n[0:length - i])
            if not is_prime(truncated):
                return False
        return True
    x = numbers[29]
    return [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]