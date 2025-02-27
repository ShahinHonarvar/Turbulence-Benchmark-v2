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
        while len(s) > 2:
            if not is_prime(int(s)) or '0' in s:
                return False
            s = s[1:-1]
        return all((is_prime(int(s[i:])) and is_prime(int(s[:len(s) - i])) for i in range(1, len(s))))
    x = numbers[39]
    result = [n for n in range(2, x + 1) if is_left_right_truncatable(n)]
    return sorted(result, reverse=True)