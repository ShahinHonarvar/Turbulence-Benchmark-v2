def all_left_right_truncatable_prime(numbers):
    x = numbers[429]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num):
        s = str(num)
        if '0' in s:
            return False
        while len(s) > 1:
            if not is_prime(int(s)) or not is_prime(int(s[::-1])):
                return False
            s = s[1:-1]
        return len(s) > 0 and is_prime(int(s))
    result = [num for num in range(10, x + 1) if is_left_right_truncatable_prime(num)]
    return sorted(result, reverse=True)