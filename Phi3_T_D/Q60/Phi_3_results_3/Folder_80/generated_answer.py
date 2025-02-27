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
    while str_n:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[:-1] if str_n[-1] == '0' else str_n[1:]
    return True

def all_left_right_truncatable_primes(nums):
    x = nums[14]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)], reverse=True)