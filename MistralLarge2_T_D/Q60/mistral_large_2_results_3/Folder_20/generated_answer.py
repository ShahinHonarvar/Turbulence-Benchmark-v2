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
    if not is_prime(n):
        return False
    num_str = str(n)
    if '0' in num_str:
        return False
    left, right = (0, len(num_str) - 1)
    while left < right:
        left_part = int(num_str[left:])
        right_part = int(num_str[:right + 1])
        if not is_prime(left_part) or not is_prime(right_part):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(data):
    x = data[100]
    truncatable_primes = [num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)