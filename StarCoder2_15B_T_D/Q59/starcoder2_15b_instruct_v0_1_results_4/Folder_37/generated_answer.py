def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_left_truncatable_prime(numbers: tuple) -> list:
    """
    Generate all left-truncatable prime numbers less than x.
    """
    x = numbers[35]
    result = []

    def helper(num: int):
        if is_prime(num):
            result.append(num)
            if num > 10:
                helper(num // 10)
    helper(x)
    return sorted(result, reverse=True)