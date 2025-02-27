def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        s = str(n)
        if len(s) <= 1:
            return False
        if not is_prime(n):
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
            if not is_prime(int(s[:i])):
                return False
        return True
    result = []
    for i in range(2, x[19] + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)