def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_left_right_truncatable(p):
        str_p = str(p)
        for i in range(len(str_p)):
            if not is_prime(int(str_p[i:])) or not is_prime(int(str_p[:len(str_p) - i])):
                return False
        return True
    x = numbers[65]
    result = [p for p in range(2, x + 1) if is_prime(p) and is_left_right_truncatable(p)]
    return sorted(result, reverse=True)