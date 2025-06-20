import math

def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s) - 1):
            if not (is_prime(int(s[i:])) and is_prime(int(s[:-i]))):
                return False
        return True
    x = numbers[97]
    result = [n for n in range(10, x + 1) if is_prime(n) and is_left_right_truncatable_prime(n)]
    return result