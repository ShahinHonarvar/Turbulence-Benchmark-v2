def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 946:
        return []
    x = numbers[945]

    def is_truncatable_prime(p):
        p_str = str(p)
        for i in range(1, len(p_str)):
            if not is_prime(int(p_str[i:])) or not is_prime(int(p_str[:-i])):
                return False
        return True
    return sorted([p for p in range(2, x + 1) if is_prime(p) and is_truncatable_prime(p)], reverse=True)