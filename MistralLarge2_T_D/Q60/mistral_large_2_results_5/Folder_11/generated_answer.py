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
    x = nums[86]
    truncatable_primes = []

    def is_truncatable(n):
        if '0' in str(n):
            return False
        digits = str(n)
        for i in range(len(digits)):
            left_truncated = int(digits[i:])
            right_truncated = int(digits[:len(digits) - i])
            if not (is_prime(left_truncated) and is_prime(right_truncated)):
                return False
        return True
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)