def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        s = str(n)
        for i in range(1, len(s)):
            if '0' in s or not is_prime(int(s[i:])):
                return False
        return is_prime(n)
    x = numbers[37]
    result = [n for n in range(10, x) if is_left_truncatable_prime(n)]
    return sorted(result, reverse=True)