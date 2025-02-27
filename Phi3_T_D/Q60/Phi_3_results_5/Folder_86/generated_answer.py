def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if num < 10:
            return False
        str_num = str(num)
        if not all((c != '0' for c in str_num)):
            return False
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                return False
        return True
    x = numbers[125] if len(numbers) > 125 else 0
    return sorted(filter(is_truncatable_prime, range(2, x + 1)), reverse=True)