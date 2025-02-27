def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True
    x = numbers[49]
    return sorted([p for p in range(2, x) if is_right_truncatable_prime(p)])