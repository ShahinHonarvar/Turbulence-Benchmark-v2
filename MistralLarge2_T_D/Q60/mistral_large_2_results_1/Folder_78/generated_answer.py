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

    def is_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        while str_num:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:-1]
        return True
    x = nums[23]
    primes = [num for num in range(2, x + 1) if is_prime(num)]
    truncatable_primes = [num for num in primes if is_truncatable(num)]
    return sorted(truncatable_primes)