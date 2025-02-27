def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(s):
        while s:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    x = numbers[93] if 93 < len(numbers) else -1
    return sorted([p for p in range(2, x) if is_left_truncatable_prime(str(p))])