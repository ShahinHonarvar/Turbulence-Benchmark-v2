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

def is_truncatable_prime(p):
    p_str = str(p)
    if len(p_str) == 1 or (len(p_str) == 2 and is_prime(int(p_str))):
        for i in range(1, len(p_str)):
            if not is_prime(int(p_str[i:])) or not is_prime(int(p_str[:-i])):
                return False
        return True
    return False

def all_left_right_truncatable_prime(nums):
    if len(nums) != 619:
        raise ValueError('Tuple must contain exactly 619 elements.')
    x = nums[618]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes