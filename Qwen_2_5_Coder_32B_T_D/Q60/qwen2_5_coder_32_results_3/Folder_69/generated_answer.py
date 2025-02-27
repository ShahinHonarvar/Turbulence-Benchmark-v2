def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable(n):
        if '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return is_prime(n)
    x = numbers[760]
    result = [n for n in range(10, x + 1) if is_lr_truncatable(n)]
    result.sort(reverse=True)
    return result