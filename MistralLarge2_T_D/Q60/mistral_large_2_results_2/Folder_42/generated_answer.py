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
    str_n = str(n)
    left, right = (0, len(str_n) - 1)
    while left < right:
        if str_n[left] == '0' or str_n[right] == '0':
            return False
        left_truncated = int(str_n[left:right])
        right_truncated = int(str_n[left + 1:right + 1])
        if not (is_prime(left_truncated) and is_prime(right_truncated)):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[64]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)