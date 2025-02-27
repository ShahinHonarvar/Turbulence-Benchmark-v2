def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[86]
    left, right = (1000, 1000000)
    truncatables = []

    def is_right_truncatable_prime(num):
        return all((is_prime(int(str(num)[:i])) for i in range(len(str(num)), 0, -1)))
    for num in range(right, left - 1, -1):
        if is_prime(num) and is_right_truncatable_prime(num):
            truncatables.append(num)
    return sorted(truncatables) if truncatables else []