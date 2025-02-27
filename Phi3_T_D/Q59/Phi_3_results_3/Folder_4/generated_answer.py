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

def all_left_truncatable_prime(nums):
    x = nums[95]
    left_truncatables = []
    for i in range(x - 1, 1, -1):
        str_i = str(i)
        if is_prime(i) and all((is_prime(int(str_i[:j])) for j in range(1, len(str_i)))):
            left_truncatables.append(i)
    return left_truncatables