def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        for i in range(1, len(s) - 1):
            if '0' in s[i:] or '0' in s[:-i]:
                return False
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    x = numbers[30]
    result = [n for n in range(10, x + 1) if is_prime(n) and is_left_right_truncatable(n)]
    return result