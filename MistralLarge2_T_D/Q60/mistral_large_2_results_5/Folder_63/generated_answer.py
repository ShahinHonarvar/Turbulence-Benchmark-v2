def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if not is_prime(n) or '0' in str(n):
        return False
    s = str(n)
    left, right = (0, len(s) - 1)
    while left < right:
        if not is_prime(int(s[left:right + 1])):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(truncatable_primes)