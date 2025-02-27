def is_left_truncatable_prime(num):
    if num < 10:
        return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
        return False
    return is_left_truncatable_prime(num // 10)