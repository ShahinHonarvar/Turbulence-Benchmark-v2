def all_left_truncatable_prime(numbers):
    x = numbers[41]

    def is_prime(n):
        if n < 2:
            return False
        for divisor in range(2, int(n ** 0.5) + 1):
            if n % divisor == 0:
                return False
        return True

    def is_truncatable_prime(p):
        p_str = str(p)
        for i in range(len(p_str)):
            if not is_prime(int(p_str[i:])):
                return False
        return True
    return sorted([p for p in range(2, x) if is_prime(p) and is_truncatable_prime(p)])