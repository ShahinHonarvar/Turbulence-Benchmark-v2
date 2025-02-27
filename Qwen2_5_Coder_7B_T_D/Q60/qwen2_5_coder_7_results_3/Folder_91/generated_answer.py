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
        for i in range(len(s)):
            if s[i] == '0' or not is_prime(int(s[i:])):
                return False
            if i > 0 and (not is_prime(int(s[:i + 1]))):
                return False
        return True
    x = numbers[0]
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)