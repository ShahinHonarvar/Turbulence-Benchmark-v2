def is_truncatable_prime(n):
    if n < 10:
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    threshold = numbers[55]
    return sorted([n for n in range(2, threshold + 1) if is_truncatable_prime(n)], reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True