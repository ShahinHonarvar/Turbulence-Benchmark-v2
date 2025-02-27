def all_left_right_truncatable_prime(numbers):
    x = numbers[93]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s) - 1):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return is_prime(n) if len(s) > 1 else True
    result = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return result