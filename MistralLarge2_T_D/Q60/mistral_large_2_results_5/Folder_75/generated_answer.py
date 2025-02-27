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

def is_left_right_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str or not is_prime(n):
        return False
    left, right = (0, len(n_str) - 1)
    while left < right:
        if not is_prime(int(n_str[left:right + 1])):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[41]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(truncatable_primes)