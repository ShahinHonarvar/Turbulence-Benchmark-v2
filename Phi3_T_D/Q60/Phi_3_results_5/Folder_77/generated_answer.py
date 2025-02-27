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

def left_and_right_truncatable_prime(n):
    return n > 1 and is_prime(n) and is_prime(n // 10) and is_prime(-(n % 10) + n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[767]
    return sorted([filter(left_and_right_truncatable_prime, range(2, x + 1))], reverse=True)[0]