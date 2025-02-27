def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    left, right = (0, len(num_str) - 1)
    while left <= right:
        if not is_prime(int(num_str[left:right + 1])):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[30]
    primes = [num for num in range(2, x + 1) if is_prime(num)]
    truncatable_primes = [num for num in primes if is_left_right_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)