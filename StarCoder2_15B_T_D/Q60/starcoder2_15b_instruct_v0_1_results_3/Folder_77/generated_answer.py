def all_left_right_truncatable_prime(numbers):
    all_truncatables = set()
    for num in numbers:
        if is_truncatable_prime(num):
            all_truncatables.add(num)
    return sorted(all_truncatables, reverse=True)

def is_truncatable_prime(num):
    if num < 10:
        return is_prime(num)
    if num % 10 == 0:
        return False
    if not is_prime(num):
        return False
    return is_truncatable_prime(num // 10)

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True