def all_left_right_truncatable_prime(numbers):
    lower_limit, upper_limit = (10, max(1, numbers[6]))

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:i])):
                return False
        return True
    return sorted([n for n in range(lower_limit, upper_limit + 1) if is_truncatable(n)], reverse=True)