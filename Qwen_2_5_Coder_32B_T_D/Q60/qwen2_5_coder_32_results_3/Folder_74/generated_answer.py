def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s) - 1):
            if not is_prime(int(s[i:-i])):
                return False
        return is_prime(n) and is_prime(int(s[1:])) and is_prime(int(s[:-1]))
    x = numbers[36]
    result = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return result