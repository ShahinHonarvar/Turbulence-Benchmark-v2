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

def is_left_and_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if not is_prime(n):
        return False
    str_n = str(n)
    return all((is_prime(int(str_n[i:])) for i in range(1, len(str_n) - 1)))

def all_left_right_truncatable_prime(numbers):
    x = numbers[26]
    return sorted([num for num in range(2, x + 1) if is_left_and_right_truncatable_prime(num)])