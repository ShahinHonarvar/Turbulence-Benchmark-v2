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
        return all((is_prime(int(s[i:])) for i in range(len(s)))) and all((is_prime(int(s[:len(s) - i])) for i in range(len(s))))
    x = numbers[29]
    result = [num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)]
    return sorted(result, reverse=True)