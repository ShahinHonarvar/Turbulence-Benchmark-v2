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

def all_left_right_truncatable_prime(nums):
    x = nums[31]
    truncatable_primes = []

    def is_truncatable(num):
        if not is_prime(num):
            return False
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                return False
        return True
    for i in range(x, 1, -1):
        if is_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)