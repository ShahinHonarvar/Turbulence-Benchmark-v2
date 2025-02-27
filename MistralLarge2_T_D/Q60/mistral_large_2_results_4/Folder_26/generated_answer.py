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
    digits = str(n)
    if '0' in digits:
        return False
    left, right = (0, len(digits))
    while left < right:
        if not is_prime(int(digits[left:right])):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(t):
    x = t[81]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)