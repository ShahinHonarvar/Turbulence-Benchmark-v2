def is_left_right_truncatable(num):
    if num < 10:
        return True
    if num < 100:
        return is_prime(num)
    if is_prime(num):
        return is_left_right_truncatable(int(str(num)[:-1]))
    return False

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

def all_left_right_truncatable_prime(numbers):
    x = numbers[78]
    return sorted(list(filter(is_left_right_truncatable, range(1, x + 1))), reverse=True)