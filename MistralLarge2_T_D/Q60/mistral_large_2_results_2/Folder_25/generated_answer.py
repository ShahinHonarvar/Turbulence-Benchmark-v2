def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[92]
    truncatable_primes = []

    def is_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        while len(str_num) > 1:
            str_num = str_num[1:-1]
            if not is_prime(int(str_num)):
                return False
        return True
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)