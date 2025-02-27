def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable(num):
    num_str = str(num)
    if not is_prime(num):
        return False
    while len(num_str) > 1:
        num_str = num_str[1:]
        if not is_prime(int(num_str)):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[41]
    truncatable_primes = []
    for num in range(1, x + 1):
        if is_left_right_truncatable(num):
            truncatable_primes.append(num)
    truncatable_primes.sort()
    return truncatable_primes