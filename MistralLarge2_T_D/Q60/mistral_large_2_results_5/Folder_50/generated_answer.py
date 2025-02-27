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

def is_left_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    str_num = str(num)
    left, right = (0, len(str_num) - 1)
    while left < right:
        if '0' in str_num:
            return False
        if left != right and (not is_prime(int(str_num[left:right + 1]))):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[57]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)