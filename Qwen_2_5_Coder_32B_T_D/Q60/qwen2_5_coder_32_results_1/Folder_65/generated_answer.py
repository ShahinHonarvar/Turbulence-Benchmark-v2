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
        for i in range(1, len(str_n) - 1):
            if not is_prime(int(str_n[i:-i])) or not is_prime(int(str_n[i:])):
                return False
        return True
    x = numbers[32]
    result = [n for n in range(10, x + 1) if is_prime(n) and is_left_right_truncatable_prime(n)]
    return result