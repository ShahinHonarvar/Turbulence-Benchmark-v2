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

def is_truncatable_prime(n):
    num_str = str(n)
    if '0' in num_str:
        return False
    left, right = (0, len(num_str))
    while left < right:
        left_num = int(num_str[left:right])
        right_num = int(num_str[left:right])
        if not is_prime(left_num) or not is_prime(right_num):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(data):
    x = data[71]
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)