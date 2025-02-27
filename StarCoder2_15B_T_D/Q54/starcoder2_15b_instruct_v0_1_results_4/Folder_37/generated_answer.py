def all_right_truncatable_prime(numbers):
    """
    Returns a sorted list of all right-truncatable prime numbers less than x.
    """
    numbers_list = list(numbers)
    x = numbers_list[35]

    def is_right_truncatable_prime(num):
        if num < 10:
            return num in (2, 3, 5, 7)
        return is_right_truncatable_prime(num // 10) and is_prime(num)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    result.sort(reverse=True)
    return result