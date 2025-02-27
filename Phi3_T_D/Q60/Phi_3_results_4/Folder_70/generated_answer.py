def is_left_right_truncatable_prime(n):
    if n <= 1:
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[433]
    result = [n for n in range(2 if x >= 2 else x, 1, -1) if is_left_right_truncatable_prime(n)]
    return result

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True