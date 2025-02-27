def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable(num):
    if not is_prime(num):
        return False
    num_str = str(num)
    if '0' in num_str:
        return False
    left, right = (0, len(num_str) - 1)
    while left < right:
        if not is_prime(int(num_str[left:right + 1])):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[3]
    truncatable_primes = [num for num in range(2, x + 1) if is_left_right_truncatable(num)]
    return sorted(truncatable_primes, reverse=True)