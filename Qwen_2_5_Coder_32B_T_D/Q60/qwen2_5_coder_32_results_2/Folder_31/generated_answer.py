def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        for i in range(1, len(str_n) - 1):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return is_prime(n)
    x = numbers[50]
    result = [num for num in range(11, x + 1) if '0' not in str(num) and is_left_right_truncatable(num)]
    return sorted(result, reverse=True)