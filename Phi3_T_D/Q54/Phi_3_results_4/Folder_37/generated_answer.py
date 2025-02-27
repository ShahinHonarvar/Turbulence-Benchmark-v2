def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_all_right_truncatable_prime(n):
    """Check if a number is a right-truncatable prime."""
    if not is_prime(n):
        return False
    str_n = str(n)
    for i in range(len(str_n) - 1, 0, -1):
        str_n = str_n[:i]
        if not is_prime(int(str_n)):
            return False
    return True

def all_right_truncatable_prime(numbers, index):
    x = numbers[index]
    return sorted([num for num in range(2, x, 2) if is_all_right_truncatable_prime(num)], reverse=True)