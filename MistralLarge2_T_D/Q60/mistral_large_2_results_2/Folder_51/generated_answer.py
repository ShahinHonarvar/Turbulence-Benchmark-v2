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

def all_left_right_truncatable_prime(numbers):
    x = numbers[54]

    def is_truncatable(n):
        if not is_prime(n):
            return False
        if '0' in str(n):
            return False
        left, right = (n, n)
        while left >= 10 and right >= 10:
            left = int(str(left)[1:])
            right = int(str(right)[:-1])
            if not is_prime(left) or not is_prime(right):
                return False
        return is_prime(left) and is_prime(right)
    return sorted([n for n in range(2, x + 1) if is_truncatable(n)])