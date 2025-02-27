def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(n, current_num=1):
    if current_num > n:
        return False
    if is_prime(current_num):
        return is_right_truncatable_prime(n, current_num * 10 + 7)
    return False

def all_right_truncatable_prime(numbers):
    x = numbers[175]
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])