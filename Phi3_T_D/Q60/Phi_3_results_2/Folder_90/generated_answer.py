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

def is_truncatable(n):
    str_n = str(n)
    return all((is_prime(n) for n in range(int(str_n[i:]), int(str_n[:i + 1]) + 1)))

def all_left_right_truncatable_prime(nums):
    x = nums[465]
    return sorted(filter(is_truncatable, range(2, x + 1)), reverse=True)